import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
n = int(input())
a = [int(input()) for i in range(n)]
b = [2 ** i for i in range(30)]
c = []
ans = [1, 1, 1, 1, 5, 1, 21, 1, 85, 73, 341, 89, 1365, 1, 5461, 4681, 21845, 1, 87381, 1, 349525, 299593, 1398101, 178481, 5592405, 1082401, 22369621, 19173961, 89478485, 2304167]
for i in range(30):
    c.append(b[i] - 1)
for i in range(n):
    if a[i] in c:
        print(ans[c.index(a[i])])
    else:
        j = 0
        while b[j] <= a[i]:
            j += 1
        print(c[j])
