n = int(input())
x = [int(input()) for _ in range(5)]
cap = min(x)
ans = (n+cap-1) // cap + 4
print(ans)

