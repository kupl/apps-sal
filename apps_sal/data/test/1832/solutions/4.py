t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = ord('a')
    s = 'a' * 200
    print(s)
    for i in range(n):
        b += 1
        if b == ord('z'):
            b = ord('a')
        s = s[:a[i]] + chr(b) * (200 - a[i])
        print(s)
