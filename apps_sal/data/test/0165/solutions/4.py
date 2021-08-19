x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
mexx = max(max(a, b), c)
mexx -= 1
ans = 0
ans += max(0, mexx - a)
ans += max(0, mexx - b)
ans += max(0, mexx - c)
print(ans)
