from collections import Counter
N = int(input())
A = list(map(int, input().split()))
AP = [0] * N
AM = [0] * N

for i in range(N):
    AP[i] = i + A[i]
    AM[i] = i - A[i]

cnt = 0
QC = Counter(AP)
for m in AM:
    cnt += QC[m]

print(cnt)
