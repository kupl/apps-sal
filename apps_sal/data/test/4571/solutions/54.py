n, m = map(int, input().split())

# １回かかる時間
submit = 1900 * m + 100 * (n - m)

ans = submit * 2**m
print(ans)
