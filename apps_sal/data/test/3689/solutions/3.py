import sys
input = sys.stdin.readline
(n, k) = list(map(int, input().split()))
A = input().strip()
A += '0' * (k - n % k)
x = A[:k]
flag = 0
for i in range(0, len(A), k):
    if A[i:i + k] > x:
        flag = 1
        break
    elif A[i:i + k] == x:
        continue
    else:
        break
if flag == 0:
    ANS = (x * (len(A) // k))[:n]
else:
    ANS = (str(int(x) + 1) * (len(A) // k))[:n]
print(len(ANS))
print(ANS)
print()
