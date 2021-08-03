k, r = list(map(int, input().split()))
x = k
ans = 1
while x % 10 != r and x % 10 != 0:
    x += k
    ans += 1
print(ans)
