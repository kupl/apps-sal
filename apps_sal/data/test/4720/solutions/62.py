N = int(input())
ans = 0
for i in range(N):
    L = input().split()
    ans += int(L[1]) - int(L[0]) + 1
print(ans)
