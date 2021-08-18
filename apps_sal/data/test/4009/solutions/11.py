n, x, y = list(map(int, input().split()))
num = input()
ans = 0
for i in range(x):
    if i == y:
        if num[n - 1 - i] != "1":
            ans += 1
    else:
        if num[n - 1 - i] != "0":
            ans += 1
print(ans)
