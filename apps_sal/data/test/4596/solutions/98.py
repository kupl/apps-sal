N = int(input())
a = list(map(int, input().split()))
ans = 0
exist = True

while exist:
    for i in range(N):
        if (a[i] % 2 != 0):
            exist = False
        else:
            a[i] = a[i] // 2
    if exist:
        ans += 1

print(ans)
