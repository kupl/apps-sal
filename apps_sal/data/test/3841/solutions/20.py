(n, a) = list(map(int, input().split()))
ar = []
j = 1
while n != 0:
    q = n % a
    n //= a
    n = -1 * n
    ar.append(q)
print(len(ar))
for i in range(len(ar)):
    print(ar[i])
