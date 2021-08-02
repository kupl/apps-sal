N = int(input())
A = list(map(int, input().split()))
m = min(A)
n = 0
while m != n:
    m = min(A)
    a = [m]
    for i in A:
        i %= m
        if i != 0:
            a.append(i)
    A = a
    n = min(A)
print(n)
