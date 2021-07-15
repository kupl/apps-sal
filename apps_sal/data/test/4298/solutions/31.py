n, d = [int(i) for i in input().split()]
ans = n // (2 * d + 1)
ans = ans if n % (2 * d + 1) == 0 else ans + 1
print(ans)
