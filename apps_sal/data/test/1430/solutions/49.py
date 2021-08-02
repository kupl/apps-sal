N, K = map(int, input().split())
S = input()
A = []
now = S[0]
if now == '0':
    A.append(0)
C = 1
for s in S[1:]:
    if s == now:
        C += 1
    else:
        A.append(C)
        now = s
        C = 1
A.append(C)
if now == '0':
    A.append(0)
B = [sum(A[:2 * K + 1])]
i = 0
j = 2 * (K + 1)
while j < len(A):
    b = B[-1] + sum(A[j - 1:j + 1]) - sum(A[i:i + 2])
    B.append(b)
    i += 2
    j += 2
print(max(B))
