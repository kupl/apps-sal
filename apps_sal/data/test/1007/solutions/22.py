k, p = map(int, input().split())

ans = 0
for i in range(1, k + 1):
    string = str(i) + str(i)[::-1]
    ans += int(string)
    ans %= p

print(ans)
