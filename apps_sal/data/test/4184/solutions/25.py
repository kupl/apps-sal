n = int(input())
w = list(map(int,input().split()))
sums = sum(w)
ans = 10000000
for i in range(n):
    a = 0
    for j in range(i):
        a += w[j]
    q = sums - a
    ans = min(ans,abs(q-a))
print(ans)
