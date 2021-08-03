d = {}
for i in range(int(input()) - 1):
    for q in input().split():
        d[q] = d.get(q, 0) + 1
print(sum(k * k - k for k in d.values()) // 2)
