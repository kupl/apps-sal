(n, t) = input().rsplit(' ')
(n, t) = (int(n), int(t))
lineWorld = [int(x) for x in input().rsplit(' ')]
start = 1
while start < t and start < n:
    oldStart = start
    start += lineWorld[start - 1]
    if start == oldStart:
        break
if start == t:
    print('YES')
else:
    print('NO')
