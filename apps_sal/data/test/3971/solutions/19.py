n = int(input())
a = list(map(int, input().split()))

counts = [0] * 100001
mx = 0
for x in a:
    counts[x] += 1
    mx = max(x, mx)

f = [0, counts[1]]
for i in range(2, mx + 1):
    f.append(max(f[i - 1], i * counts[i] + f[i - 2]))
print(f[mx])
