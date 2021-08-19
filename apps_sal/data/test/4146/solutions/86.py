from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
D1 = defaultdict(int)
D2 = defaultdict(int)
for i in range(0, N, 2):
    D1[A[i]] += 1
for i in range(1, N, 2):
    D2[A[i]] += 1
D1_sorted = sorted(D1.items(), key=lambda x: x[1], reverse=True) + [(-1, 0)]
D2_sorted = sorted(D2.items(), key=lambda x: x[1], reverse=True) + [(-1, 0)]
(i, j) = (0, 0)
while i < len(D1_sorted) - 1 and j < len(D2_sorted) - 1:
    if D1_sorted[i][0] != D2_sorted[j][0]:
        break
    elif D1_sorted[i][1] > D2_sorted[j][1]:
        j += 1
    elif D1_sorted[i][1] < D2_sorted[j][1]:
        i += 1
    elif D1_sorted[i + 1][1] > D2_sorted[j + 1][1]:
        i += 1
    else:
        j += 1
print(N - D1_sorted[i][1] - D2_sorted[j][1])
