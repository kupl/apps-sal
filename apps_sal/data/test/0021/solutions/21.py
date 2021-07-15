n = int(input())
A = list(map(int, input().split()))
mini = 0
maxi = 0
maxim = 0
minim = 10 ** 10
for i in range(n):
    if A[i] > maxim:
        maxim = A[i]
        maxi = i
    if A[i] < minim:
        minim = A[i]
        mini = i
a = abs(n - mini - 1)
b = abs(0 - mini)
c = abs(n - maxi - 1)
d = abs(0 - maxi)
print(max(a, b, c, d))
