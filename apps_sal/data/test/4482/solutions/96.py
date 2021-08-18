N = int(input())
aN = list(map(int, input().split()))
S = 0
A = 0
for i in aN:
    S += i
A = S / N
if A - int(A) < 0.5:
    A = int(A)
else:
    A = int(A) + 1
R = 0
for i in aN:
    R += (i - A)**2
print(R)
