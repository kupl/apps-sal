import sys as _sys


def main():
    n, = _read_ints()
    a = tuple(_read_ints())
    m, = _read_ints()
    queries = (tuple(_read_ints()) for i_query in range(m))
    result = process_queries(a, queries)
    print(*result, sep='\n')


def _read_line():
    result = _sys.stdin.readline()
    assert result[-1] == "\n"
    return result[:-1]


def _read_ints():
    return map(int, _read_line().split())


def process_queries(sequence, queries):
    sequence = tuple(sequence)

    indices_to_select = sorted(
        range(len(sequence)),
        key=lambda index: (-sequence[index], index)
    )

    enumerated_queries = sorted(enumerate(queries), key=lambda iv: iv[1][0])[::-1]
    queries_responses = [None] * len(enumerated_queries)

    selections_tree = [0] * (len(sequence) + 1)

    selected_n = 0
    for index_to_select in indices_to_select:
        _fenwick_tree_add(selections_tree, index_to_select, 1)
        selected_n += 1
        while enumerated_queries and enumerated_queries[-1][1][0] == selected_n:
            query_index, (_k, subseq_index) = enumerated_queries.pop()
            seq_index = _find_seq_index_by_subseq_index(selections_tree, subseq_index)
            queries_responses[query_index] = sequence[seq_index]

    return queries_responses


def _find_seq_index_by_subseq_index(tree, subseq_i):
    seq_length = len(tree) - 1
    min_i = 0
    max_i = seq_length - 1
    while min_i != max_i:
        mid_i = (min_i + max_i) // 2
        if _fenwick_tree_prefix_sum(tree, mid_i) < subseq_i:
            min_i = mid_i + 1
        else:
            max_i = mid_i
    return min_i


def _fenwick_tree_prefix_sum(tree, i):
    i += 1
    result = 0
    while i != 0:
        result += tree[i]
        i -= i & (-i)
    return result


def _fenwick_tree_add(tree, i, x):
    i += 1
    while i < len(tree):
        tree[i] += x
        i += i & (-i)


def __starting_point():
    main()


__starting_point()
