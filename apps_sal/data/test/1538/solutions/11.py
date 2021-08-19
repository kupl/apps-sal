n = int(input())
A = [int(i) for i in input().split(' ')]
res = 1
A.sort()
res = 0
for i in A:
    res = max(res, A.count(i))
print(res)
'\n2 3 4 2 3 4\n1 1 1 2 2 2\n'
