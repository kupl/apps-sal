(a, b) = [int(i) for i in input().split()]
ans = (b - 1) // (a - 1) + 1 if (b - 1) % (a - 1) else (b - 1) // (a - 1)
print(ans)
