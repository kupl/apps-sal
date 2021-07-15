n = int(input())
t = list(map(int, input().split()))
res = [0] * n
for i in range(n):
    temp = [0] * n
    idx = -1
    max_freq = 0
    for j in range(i, n):
        if temp[t[j] - 1] + 1 > max_freq:
            max_freq += 1
            idx = t[j]
        elif temp[t[j] - 1] + 1 == max_freq and t[j] < idx:
            idx = t[j]
        temp[t[j] - 1] += 1
        res[idx - 1] += 1
print(*res)

