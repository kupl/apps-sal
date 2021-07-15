import copy
n = int(input())
t = [int(x) for x in input().split()]
m = int(input())
for i in range(m):
    p, x = map(int, input().split())
    t_temp = copy.copy(t)
    t_temp[p - 1] = x
    print(sum(t_temp))
