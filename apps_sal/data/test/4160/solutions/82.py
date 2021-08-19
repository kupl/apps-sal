X = int(input())
ans = 0
m = 100
while m < X:
    m = m * 101 // 100
    ans += 1
print(ans)
