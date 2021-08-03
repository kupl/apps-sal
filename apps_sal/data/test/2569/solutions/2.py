def gns():
    return list(map(int, input().split()))


t = int(input())
ns = []
ans = [0, 0, 0, 4, 4, 12]
for _ in range(t):
    n = int(input())
    ns.append(n)
mx = max(ns)
md = 10**9 + 7
for i in range(6, mx + 6):
    ans.append((ans[-2] * 2 + ans[-1] + (4 if i % 3 == 0 else 0)) % md)
for ni in ns:
    print(ans[ni])
