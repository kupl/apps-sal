n = int(input())
A = sorted(int(input())for _ in range(n))
B = 10007
s = 0
for i in range(n):
    s = (A[i] * A[-1 - i] + s) % B
print(s)
