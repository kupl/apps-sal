import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
A = [0] * n
k = n // 3
c0 = 0
c1 = 0
c2 = 0
for i in range(0, n):
    if s[i] == '0':
        c0 = c0 + 1
    elif s[i] == '1':
        c1 = c1 + 1
    else:
        c2 = c2 + 1
    A[i] = s[i]

i = 0
while c0 < k:
    if (A[i] == '1' and c1 > k):
        A[i] = '0'
        c0 = c0 + 1
        c1 = c1 - 1
    elif (A[i] == '2' and c2 > k):
        A[i] = '0'
        c0 = c0 + 1
        c2 = c2 - 1
    i = i + 1
i = n - 1
while c0 > k and c2 < k:
    if A[i] == '0':
        A[i] = '2'
        c0 = c0 - 1
        c2 = c2 + 1
    i = i - 1
while c0 > k and c1 < k:
    if A[i] == '0':
        A[i] = '1'
        c0 = c0 - 1
        c1 = c1 + 1
    i = i - 1
i = n - 1
while c1 > k and c2 < k:
    if A[i] == '1':
        A[i] = '2'
        c1 = c1 - 1
        c2 = c2 + 1
    i = i - 1
i = 0
while c1 < k and c2 > k:
    if A[i] == '2':
        A[i] = '1'
        c2 = c2 - 1
        c1 = c1 + 1
    i = i + 1

print("".join(A))
