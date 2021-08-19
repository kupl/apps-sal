n = int(input())
counts = [0] * 100002
for a in map(int, input().split()):
    counts[a] += 1

f2, f1 = 0, counts[1]  # f[i-2], f[i-1]
for i in range(2, 100002):
    f2, f1 = f1, max(f1, i * counts[i] + f2)
print(f1)
