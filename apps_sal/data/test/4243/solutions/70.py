x = int(input())
ans = (x // 500) * 1000
ans += (x % 500) // 5 * 5
print((str(ans)))
