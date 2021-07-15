from collections import Counter

N = input()
A = list(map(int, input().split()))

counter = Counter(A)

cnt = 0
for k, v in list(counter.items()):
    if v < k:
        cnt += v
    elif v > k:
        cnt += v - k


print(cnt)

