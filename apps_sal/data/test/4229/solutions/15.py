N = int(input())

ans = 0
for i in range(N + 1):
    if i % 5 == 0 or i % 3 == 0:
        ans = ans
    else:
        ans += i

print(ans)
