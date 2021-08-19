(n, m, k) = list(map(int, input().split(' ')))
a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]
A = [0]
B = [0]
for i in a:
    if A[-1] > k:
        break
    A.append(A[-1] + i)
for i in b:
    if B[-1] > k:
        break
    B.append(B[-1] + i)
ans = 0
j = len(B) - 1
for i in range(len(A)):
    if A[i] > k:
        break
    while A[i] + B[j] > k:
        j -= 1
    ans = max(ans, i + j)
print(ans)
