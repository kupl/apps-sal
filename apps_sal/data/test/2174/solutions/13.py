n = int(input())
seq = sorted(list(map(int, input().split())))
res = 0
for i in range(n):
    res += abs(seq[i] - (i + 1))
print(res)
