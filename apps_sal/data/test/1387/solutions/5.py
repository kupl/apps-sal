# input
n, t = map(int, input().split())
a = [int(x) for x in input().split()]

# variables
p = 1

# main
while p <= t:
    if p == t:
        print('YES')
        quit()
    p += a[p - 1]

# output
print('NO')
