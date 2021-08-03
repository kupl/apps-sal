n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 0:
        print(0)
        return
tmp = 1
for i in range(n):
    if a[i] <= (int(1e18) // tmp):
        tmp *= a[i]
    else:
        print(-1)
        return
print(tmp)
