import sys
input = sys.stdin.readline
n = int(input())
d = int(input())
e = int(input())
D = d * 1
E = e * 5
x = n % D
ANS = x
for i in range(x, min(n, x + D * 1000) + 1, D):
    ANS = min(ANS, i % E)
print(ANS)
