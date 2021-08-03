import copy
n = int(input())
t = list(map(int, input().split()))
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    total = copy.copy(t)
    total[a - 1] = b
    print(sum(total))
