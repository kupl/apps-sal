(l, r, k) = map(int, input().split())
_k = int(k)
k = 1
ans = 0
ok = 0
while k <= r:
    if k >= l:
        print(k, end=' ')
        ok = 1
    k *= _k
if ok == 0:
    print(-1)
