n = int(input())
z = list(map(int, input().split()))
ans = 0
now = 0
for i in range(n):
    if z[i] == 4 or z[i] == 5:
        now += 1
        ans += now // 3
        now %= 3
    else:
        now = 0
print(ans)
