"""
"""
from operator import itemgetter


def on_segments_own_points(segment_list) -> int:
    (alexey_l, alexey_r) = segment_list[0]
    if len(segment_list) == 1:
        return alexey_r - alexey_l
    segment_list.sort(key=itemgetter(0))
    (l_curr, r_curr) = segment_list[0]
    i = 0
    while not (l_curr == alexey_l and r_curr == alexey_r):
        i += 1
        (l_curr, r_curr) = segment_list[i]
    if i > 0:
        (l_curr, r_curr) = max(segment_list[:i], key=itemgetter(1))
        if r_curr >= alexey_r:
            return 0
        elif alexey_l <= r_curr < alexey_r:
            start = r_curr
        else:
            start = alexey_l
    else:
        start = alexey_l
    non_overlapped = 0
    for j in range(i + 1, len(segment_list)):
        (l_curr, r_curr) = segment_list[j]
        if start < l_curr:
            if l_curr < alexey_r:
                non_overlapped += l_curr - start
                if r_curr > alexey_r:
                    return non_overlapped
                else:
                    start = r_curr
            else:
                return alexey_r - start
        elif start > r_curr:
            continue
        elif r_curr < alexey_r:
            start = r_curr
        else:
            return non_overlapped
    if start < alexey_r:
        return non_overlapped + alexey_r - start
    return non_overlapped


def __starting_point():
    """
    Inside of this is the test. 
    Outside is the API
    """
    n = int(input())
    segments = [tuple(map(int, input().split())) for i in range(n)]
    print(on_segments_own_points(segments))


__starting_point()
