import sys
for _ in range(int(input())):
    (n, k) = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))
    s = sum(a)
    if s % 2 == 0 and k % 2 or (s % 2 and k % 2 == 0):
        print('NO')
    else:
        s = 0
        b = []
        i = 0
        j = 0
        while i < k - 1 and j < n:
            if s % 2 == 0:
                s += a[j]
                j += 1
            else:
                b.append(j)
                s = 0
                i += 1
        b.append(n)
        if len(set(b)) == k:
            print('YES')
            print(*b)
        else:
            print('NO')
