N = int(input())
lsa = list(map(int,input().split()))
ans = 0
for i in range(N):
    a = lsa[i]
    while a % 2 == 0:
        ans += 1
        a = a//2
print(ans)
