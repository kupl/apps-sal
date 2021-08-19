(a, b, c) = [int(i) for i in input().split()]
ans = c - (a - b)
ans = ans if ans >= 0 else 0
print(ans)
