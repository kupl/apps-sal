import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    (a, b) = (a[n - 1::-1], a[n:])
    (ma, mb) = ({0: 0}, {0: 0})
    pa = pb = 0
    for i in range(n):
        pa += 1 if a[i] == 1 else -1
        pb += 1 if b[i] == 1 else -1
        if pa not in ma:
            ma[pa] = i + 1
        if pb not in mb:
            mb[pb] = i + 1
    total = pa + pb
    ans = 10 ** 9
    for (da, va) in list(ma.items()):
        req = total - da
        if req in mb:
            ans = min(ans, va + mb[req])
    print(ans)
