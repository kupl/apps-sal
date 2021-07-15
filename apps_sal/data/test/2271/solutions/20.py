n = int(input())
bounds_amount = [-1]*n
for _ in range(n-1):
    for el in map(int, input().split(' ')): bounds_amount[el-1] += 1
print(sum(map(lambda x: (x*(x+1))//2, bounds_amount)))
