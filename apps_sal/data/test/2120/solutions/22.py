t = input().split()
n = int(t[0])
m = int(t[1])
slon = 0
num = [int(x) for x in input().split()]
for i in range(m):
    t = input().split()
    slon += min(num[int(t[0]) - 1], num[int(t[1]) - 1])
print(slon)
