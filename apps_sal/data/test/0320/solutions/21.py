n = int(input())
(A, B, C) = (0, 0, 0)
for i in range(n):
    (a, b) = map(int, input().split())
    A += a
    B += b
    if a % 2 != b % 2:
        C = 1
if A % 2 == 0 and B % 2 == 0:
    print(0)
elif A % 2 == 1 and B % 2 == 1 and C:
    print(1)
else:
    print(-1)
