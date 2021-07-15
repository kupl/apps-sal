def main():
    import collections
    n, m = list(map(int, input().split()))
    hs = list(map(int, input().split()))
    nmap = [0] * n
    cnt = 0

    for j in range(m):
        v = input().split()
        v0 = int(v[0]) - 1
        v1 = int(v[1]) - 1
        if hs[v0] < hs[v1]:
            nmap[v0] += 1
        elif hs[v0] == hs[v1]:
            nmap[v0] += 1
            nmap[v1] += 1
        else:
            nmap[v1] += 1
    for i in nmap:
        if i == 0:
            cnt += 1
    return cnt


def __starting_point():
    print((main()))

__starting_point()
