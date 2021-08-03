n = int(input())

ans = "NO"

for i in range(n):
    L = list(input().split())
    if (int(L[1]) >= 2400 and int(L[2]) > int(L[1])):
        ans = "YES"
print(ans)
