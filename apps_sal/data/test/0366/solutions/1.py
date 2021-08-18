n, m = map(int, input().split())
ans = m // n + min(1, m % n)
print(ans)
