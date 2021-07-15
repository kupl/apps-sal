x, y = list(map(int, input().split()))

res = 0
base = 1
while(x*base <= y):
    base *= 2
    res += 1

print(res)

