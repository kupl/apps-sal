(x, y) = map(int, input().split())
ans = 1
total = x
while total < y:
    ans += 1
    total += x
    total -= 1
print(ans if y != 1 else 0)
