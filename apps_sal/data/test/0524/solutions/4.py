n = int(input())
b = list(map(int, input().split()))
b.sort()
val = b[-1] ** (1 / (n - 1))
pos1 = int(val)
pos2 = int(val) + 1
val1 = 0
val2 = 0
for i in range(n):
    val1 += abs(b[i] - pos1 ** i)
    val2 += abs(b[i] - pos2 ** i)
print(min(val1, val2))
