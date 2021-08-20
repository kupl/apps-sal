from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
A = set(A)
B = [True] * (10 ** 6 + 1)
for a in A:
    for i in range(2 * a, 10 ** 6 + 1, a):
        B[i] = False
cnt = 0
for a in A:
    if B[a] == True and C[a] == 1:
        cnt += 1
print(cnt)
