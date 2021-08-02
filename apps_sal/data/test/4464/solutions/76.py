a, b, c = map(int, input().split())
res = 0
for i in range(1, 101):
    if (a * i) % b == c:
        res += 1

print("YES") if res > 0 else print("NO")
