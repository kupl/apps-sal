n = int(input())
reds = sorted([list(map(int, input().split())) for i in range(n)], key=lambda reds: -reds[1])
blues = sorted([list(map(int, input().split())) for i in range(n)])
res = 0
for (c, d) in blues:
    for (a, b) in reds:
        if a < c and b < d:
            reds.remove([a, b])
            res += 1
            break
print(res)
