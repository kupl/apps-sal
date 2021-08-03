N = int(input())
A = list(map(int, input().split()))
P = [0 for n in range(N)]
B = [True for n in range(N)]
for n in range(N):
    P[n] += -1
    P[max(0, n - A[n])] += 1
total = 0
for n in range(N):
    if n > 0:
        P[n] += P[n - 1]
    if P[n] > 0:
        B[n] = False

for n in range(N):
    if B[n]:
        total += 1
print(total)
