X = int(input())
n = 100
ans = 0
while n < X:
    n += n // 100
    ans += 1
print(ans)
