from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

cnt = 0
for v in C.values():
    if v > 1:
        cnt += v - 1

if cnt % 2 == 0:
    print(N - cnt)
else:
    print(N - cnt - 1)
