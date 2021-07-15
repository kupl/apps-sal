from bisect import bisect_left
n, q = map(int, input().split())
s = list(input())
L = []
for i in range(n - 1):
    if s[i] == "A" and s[i + 1] == "C":
        L.append(i)
ans = []
for i in range(q):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    st = bisect_left(L, l)
    fi = bisect_left(L, r)
    ans.append(fi - st)

for i in ans:
    print(i)
