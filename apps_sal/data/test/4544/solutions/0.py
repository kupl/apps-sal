n = int(input())
a = list(map(int, input().split()))
d = [0] * (10 ** 5 + 10)
for av in a:
    for x in [-1, 0, 1]:
        d[av + x + 1] += 1
print(max(d))
