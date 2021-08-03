a, b, x = map(int, input().split())

if a == 0:
    ans = b // x + 1
else:
    ans = b // x - (a - 1) // x
print(ans)
