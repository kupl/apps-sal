N = int(input())
P = [int(i) for i in input().split()]
ans = 0
a = N
for i in range(N):
    if(P[i] <= a):
        ans += 1
        a = min(a, P[i])
        continue
    a = min(a, P[i])
print(ans)
