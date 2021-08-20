n = int(input())
A = list(map(int, input().split()))
B = [n] + [0] * (n + 1)
C = {}
calcset = set()
good = 0
next = 0
for i in range(n):
    C[A[i]] = C.get(A[i], 0) + 1
    B[C[A[i]] - 1] -= 1
    B[C[A[i]]] += 1
    if C[A[i]] > next:
        next = C[A[i]]
    calcset.add(A[i])
    if B[next] + B[next - 1] == len(calcset) and B[next] == 1 or (B[1] == 1 and B[next] == len(calcset) - 1) or (next == 1 and B[next] == len(calcset)):
        good = max(good, i)
print(good + 1)
