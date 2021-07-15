import sys

try:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
except:
    pass

n, m = (int(i) for i in input().split())
str = [input() for i in range(0, n)]
arr = []
for i in range(0, n):
    t1, t2 = 0, 0
    for j in range(0, m):
        if str[i][j] == 'G':
            t1 = j
        elif str[i][j] == 'S':
            t2 = j
    if t1 > t2:
        print(-1)
        return
    if t1 < t2:
        arr.append(t2 - t1)
arr.sort()
answer = 0
if (len(arr) > 0):
    answer += 1
for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        answer += 1
print(answer)
