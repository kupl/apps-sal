n = int(input())
(T, A) = map(int, input().split())
H = list(map(int, input().split()))
TH = []
for i in range(n):
    TH.append(abs(A - T + 0.006 * H[i]))
print(TH.index(min(TH)) + 1)
