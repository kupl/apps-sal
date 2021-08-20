N = int(input())
(T, A) = map(int, input().split())
H = list(map(int, input().split()))
HT = [0] * N
for i in range(len(H)):
    HT[i] = T - H[i] * 0.006
sa = [float('inf')] * N
for i in range(N):
    sa[i] = float(abs(A - HT[i]))
print(sa.index(min(sa)) + 1)
