n = int(input())
d = [int(i) for i in input().split()]
d = sorted(d, reverse=True)
for i in range(1, len(d)):
    d[i] = max(0, min(d[i - 1] - 1, d[i]))
print(sum(d))
