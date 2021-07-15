n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

ans = 0
for i in range(n):
    t1 = min(aa[i], bb[i])
    aa[i] -= t1
    bb[i] -= t1
    ans += t1
    t2 = min(aa[i+1], bb[i])
    aa[i+1] -= t2
    ans += t2
print(ans)

