def edge_intersects(edge, l):
    for other_edge in l:
        if min(other_edge) < min(edge) and max(other_edge) > min(edge) and (max(other_edge) < max(edge)):
            return True
        if min(other_edge) < max(edge) and min(other_edge) > min(edge) and (max(other_edge) > max(edge)):
            return True
    return False


def intersects(l):
    edges = [(l[i], l[i + 1]) for i in range(0, len(l) - 1)]
    for i in range(len(edges) - 1):
        if edge_intersects(edges[i], edges[i + 1:]) == True:
            return True
    return False


n = input()
l = [int(item) for item in input().split()]
if intersects(l):
    print('yes')
else:
    print('no')
