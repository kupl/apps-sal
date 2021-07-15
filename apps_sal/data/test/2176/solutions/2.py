import sys

p = 998244353
n = int(sys.stdin.readline())
S1 = []
S2 = []
A = []
for i in range (0, n):
    x, y = list(map(int, sys.stdin.readline().strip().split()))
    S1.append(x)
    S2.append(y)
    A.append(x * 1000000 + y)
S1.sort()
S2.sort()
A.sort()
x = S1[0]
c = 1
ans1 = 1
for i in range (1, n):
    if S1[i] == x:
        c = c + 1
        ans1 = (ans1 * c) % p
    else:
        x = S1[i]
        c = 1
c = 1
ans2 = 1
x = S2[0]
for i in range (1, n):
    if S2[i] == x:
        c = c + 1
        ans2 = (ans2 * c) % p
    else:
        x = S2[i]
        c = 1
c = 1
ans3 = 1
x = A[0]
for i in range (1, n):
    if A[i] == x:
        c = c + 1
        ans3 = (ans3 * c) % p
    else:
        x = A[i]
        c = 1
    if A[i] % 1000000 < A[i-1] % 1000000:
        ans3 = 0
ans4 = 1
for i in range (1, n + 1):
    ans4 = ans4 * i % p
print((ans4 - ans1 -ans2 + ans3) % p)


    


