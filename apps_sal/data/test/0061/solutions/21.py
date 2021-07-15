n1 = 0
n, b = list(map(int, input().split()))
a = list(map(int, input().split()))
a.reverse()
for i in range(n):
    n1 += a[i] * (b ** i)
n2 = 0
n, b = list(map(int, input().split()))
a = list(map(int, input().split()))
a.reverse()
for i in range(n):
    n2 += a[i] * (b ** i)
if n1 < n2:
    print("<")
if n1 == n2:
    print("=")
if n1 > n2:
    print(">")

