from collections import Counter
n = int(input())
k = list(map(int, input().split()))
cnt = Counter(k)
exp = [2 ** i for i in range(32)]
pair = 0
for i in k:
    if cnt[i] > 0:
        cnt[i] -= 1
    for j in exp:
        if j - i in cnt:
            pair += cnt[j - i]
print(pair)

