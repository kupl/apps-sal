(n, m) = list(map(int, input().split()))
a = [int(e) for e in input().split()]
b = [int(e) for e in input().split()]
(A, B, C, D) = (0, 0, 0, 0)
for i in a:
    if i % 2 == 0:
        A += 1
    else:
        B += 1
for i in b:
    if i % 2 == 0:
        C += 1
    else:
        D += 1
print(min(A, D) + min(B, C))
