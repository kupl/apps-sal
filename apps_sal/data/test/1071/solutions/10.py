a1, a2, a3 = list(map(int, input().split()))
b1, b2, b3 = list(map(int, input().split()))
n = int(input())
A = a1 + a2 + a3
B = b1 + b2 + b3
n1 = A // 5
if A % 5 > 0:
    n1 += 1
n2 = B // 10
if B % 10 > 0:
    n2 += 1
if n1 + n2 <= n:
    print("YES")
else:
    print("NO")
