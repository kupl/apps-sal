n = int(input())
a = list(map(int, input().rstrip().split()))
if n == 1:
    print(a[0])
else:
    b = a + a
    k = (n+1)//2
    s = 0
    for j in range(0, 2*k, 2):
        s += b[j]
    M = s
    left = 0
    while left + 2*k < 2*n:
        s -= b[left]
        s += b[left + 2*k]
        M = max(s, M)
        left += 2
    s = 0
    for j in range(1, 2*k+1, 2):
        s += b[j]
    M = max(s, M)
    left = 1
    while left + 2*k < 2*n:
        s -= b[left]
        s += b[left + 2*k]
        M = max(s, M)
        left += 2
    print(M)
