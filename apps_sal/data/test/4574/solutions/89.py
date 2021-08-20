from collections import Counter


def solve():
    c = Counter(arr)
    four_edges = [k for (k, v) in list(c.items()) if v >= 4]
    two_edges = [k for (k, v) in list(c.items()) if 1 < v < 4]
    four_edges.append(0)
    two_edges.append(0)
    four_edges.sort(reverse=True)
    two_edges.sort(reverse=True)
    area_f = four_edges[0] * four_edges[0]
    if len(two_edges) >= 2:
        area_t = two_edges[0] * two_edges[1]
    else:
        area_t = 0
    area_t_t = two_edges[0] * four_edges[0]
    max_area = max(area_f, max(area_t, area_t_t))
    return max_area


N = int(input())
arr = list(map(int, input().split()))
res = solve()
print(res)
