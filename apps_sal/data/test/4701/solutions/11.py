n = int(input())
k = int(input())

tmp = 1
for i in range(n):
    tmp = min(tmp * 2, tmp + k)
print(tmp)
