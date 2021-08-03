a, b = map(int, input().split())
A = [1]
for i in range(2, int(a**0.5) + 1):
    if a % i == 0:
        while a % i == 0:
            a //= i
        A.append(i)
if a > 1:
    A.append(a)
B = [1]
for i in range(2, int(b**0.5) + 1):
    if b % i == 0:
        while b % i == 0:
            b //= i
        B.append(i)
if b > 1:
    B.append(b)
can = 0
for i in A:
    if i in B:
        can += 1
print(can)
