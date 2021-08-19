from sys import stdin, stdout
n = int(stdin.readline().rstrip())
leftCount = 0
rightCount = 0
for _ in range(n):
    (x, y) = list(map(int, stdin.readline().rstrip().split()))
    if x > 0:
        rightCount += 1
    else:
        leftCount += 1
if rightCount <= 1 or leftCount <= 1:
    print('Yes')
else:
    print('No')
