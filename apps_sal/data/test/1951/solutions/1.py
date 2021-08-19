from collections import defaultdict as _defaultdict
import sys as _sys


def main():
    (n,) = _read_ints()
    events = _read_events(2 * n)
    try:
        result = restore_shurikens_order(events, n)
    except ValueError:
        print('NO')
    else:
        print('YES')
        print(*result)


def _read_events(events_n):
    for i_event in range(events_n):
        (event_type, *event_args) = _read_line().split(' ')
        if event_type == '+':
            assert len(event_args) == 0
            event = (PLACE_SHURIKEN_ID,)
        else:
            assert event_type == '-'
            assert len(event_args) == 1
            event = (BUY_SHURIKEN_ID, int(event_args[0]))
        yield event


PLACE_SHURIKEN_ID = 0
BUY_SHURIKEN_ID = 1


def restore_shurikens_order(events, shurikens_n):
    result = [None] * shurikens_n
    limits_tree = [0] * (shurikens_n + 1 + 1)
    limits_counter = _defaultdict(int)
    sources_by_limits = [[] for limit in range(shurikens_n + 1)]
    next_placement_index = 0
    for event in events:
        if event[0] == PLACE_SHURIKEN_ID:
            limit = 1
            _fenwick_add(limits_tree, limit, 1)
            sources_by_limits[limit].append(next_placement_index)
            limits_counter[limit] += 1
            next_placement_index += 1
        else:
            assert event[0] == BUY_SHURIKEN_ID
            item_to_buy = event[1]
            if _fenwick_prefix_sum(limits_tree, item_to_buy) == 0:
                raise ValueError('unable to restore shurikens order')
            limits_can_be_removed_n = _fenwick_prefix_sum(limits_tree, item_to_buy)
            min_limit_to_remove = 1
            max_limit_to_remove = item_to_buy
            while min_limit_to_remove != max_limit_to_remove:
                mid_limit_to_remove = min_limit_to_remove + max_limit_to_remove >> 1
                if limits_can_be_removed_n - _fenwick_prefix_sum(limits_tree, mid_limit_to_remove) == 0:
                    max_limit_to_remove = mid_limit_to_remove
                else:
                    min_limit_to_remove = mid_limit_to_remove + 1
            limit_to_remove = min_limit_to_remove
            _fenwick_add(limits_tree, limit_to_remove, -1)
            result[sources_by_limits[limit_to_remove].pop()] = item_to_buy
            limits_counter[limit_to_remove] -= 1
            moved_limits = _fenwick_move_all_before_to(limits_tree, item_to_buy)
            for limit in moved_limits:
                moved_n = limits_counter[limit]
                del limits_counter[limit]
                limits_counter[item_to_buy] += moved_n
                assert moved_n > 0
                sources_from = sources_by_limits[limit]
                sources_to = sources_by_limits[item_to_buy]
                assert len(sources_from) == moved_n
                if len(sources_from) > len(sources_to):
                    (sources_to, sources_from) = (sources_from, sources_to)
                    (sources_by_limits[item_to_buy], sources_by_limits[limit]) = (sources_to, sources_from)
                sources_to.extend(sources_from)
                sources_from.clear()
    return result


def _fenwick_prefix_sum(tree, index):
    index += 1
    result = 0
    while index != 0:
        result += tree[index]
        index -= index & -index
    return result


def _fenwick_add(tree, index, value):
    index += 1
    while index < len(tree):
        tree[index] += value
        index += index & -index


def _fenwick_move_all_before_to(tree, index_arg):
    index_arg += 1
    planned_additions = []
    index = index_arg
    while index < len(tree):
        father_last_i = index - (index & -index)
        segment_begin = father_last_i + 1
        planned_additions.append((index, _fenwick_prefix_sum(tree, segment_begin - 1 - 1)))
        index += index & -index
    queue_to_make_segments_zero = []
    i = index_arg - 1
    while i != 0:
        if tree[i] != 0:
            queue_to_make_segments_zero.append(i)
        i -= i & -i
    i_queue = 0
    while i_queue < len(queue_to_make_segments_zero):
        i = queue_to_make_segments_zero[i_queue]
        sum_in_that_segment_except_last = 0
        last_i_digit = i & -i
        j = i - (last_i_digit >> 1)
        if j != i:
            if tree[j] != 0:
                queue_to_make_segments_zero.append(j)
                sum_in_that_segment_except_last += tree[j]
            while j & 1 != 1:
                j += (j & -j) >> 1
                if tree[j] != 0:
                    queue_to_make_segments_zero.append(j)
                    sum_in_that_segment_except_last += tree[j]
        if i & 1 == 1 or tree[i] - sum_in_that_segment_except_last != 0:
            yield (i - 1)
        tree[i] = 0
        i_queue += 1
    for (index, value_to_add) in planned_additions:
        tree[index] += value_to_add


def _read_line():
    result = _sys.stdin.readline()
    assert result[-1] == '\n'
    return result[:-1]


def _read_ints():
    return list(map(int, _read_line().split()))


def __starting_point():
    main()


__starting_point()
