(n, m, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.reverse()
inb = 0
box = 0
i = 0
while box < m and i < n:
    if inb + A[i] <= k:
        inb += A[i]
        i += 1
    else:
        box += 1
        inb = 0
print(i)
