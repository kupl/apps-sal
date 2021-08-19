import collections


def solve():
    comments = input().split(',')
    comments_by_depth = collections.defaultdict(list)
    current_depth = 0
    current_depth_limit = [10000000]
    cur_cmt = [0] * 2
    for (i, item) in enumerate(comments):
        cur_cmt[i % 2] = item
        if i % 2 == 1:
            while current_depth_limit[-1] == 0:
                current_depth_limit.pop()
                current_depth -= 1
            text = cur_cmt[0]
            child_count = int(cur_cmt[1])
            comments_by_depth[current_depth].append(text)
            current_depth_limit[-1] -= 1
            if child_count > 0:
                current_depth += 1
                current_depth_limit.append(child_count)
    depths = list(sorted(comments_by_depth.keys()))
    if depths:
        print(depths[-1] + 1)
    else:
        print(0)
    for d in depths:
        print(' '.join(comments_by_depth[d]))


def __starting_point():
    solve()


__starting_point()
