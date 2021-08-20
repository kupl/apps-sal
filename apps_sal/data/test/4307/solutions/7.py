N = int(input())
cnt = [0] * (N + 1)
for i in range(1, N + 1):
    j = i
    while j <= N:
        cnt[j] += 1
        j += i
res = 0
for i in range(1, N + 1):
    if i & 1 and cnt[i] == 8:
        res += 1
print(res)
