A, B = map(int, input().split())

x = A * B

if A < B:
    A, B = B, A

p = A % B
while p != 0:
    A, B = B, p
    p = A % B

print(round(x / B))
