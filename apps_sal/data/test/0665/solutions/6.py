import sys


# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
reader = (list(map(int, line.split())) for line in sys.stdin)
input = reader.__next__

t, = input()
for _ in range(t):
    n, s = input()
    a = list(input())
    i = 0
    left = 0
    maxSt = 0
    maxId = -1
    while i < n:
        left += a[i]
        if maxSt < a[i]:
            maxSt = a[i]
            maxId = i
        if left > s:
            break
        i += 1
    if i == n:
        print(0)
    else:
        print(maxId + 1)

# inf.close()
