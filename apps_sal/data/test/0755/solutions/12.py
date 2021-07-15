n = int(input())

ans = 0

ans += n // 5
n = n % 5
ans += n // 4
n = n % 4
ans += n // 3
n = n % 3
ans += n // 2
n = n % 2
ans += n // 1
n = n % 1

print(ans)
