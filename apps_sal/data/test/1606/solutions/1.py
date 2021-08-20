from sys import stdin
input = stdin.readline
n = int(input())
arr = list((list(map(int, input().split())) for _ in range(n)))
(curr, res) = (0, [])
for i in range(n):
    for j in range(n):
        if i == j:
            curr ^= arr[i][j]
q = int(input())
for _ in range(q):
    s = input()
    if s[0] == '3':
        res.append(str(curr))
    else:
        curr ^= 1
print(''.join(res))
