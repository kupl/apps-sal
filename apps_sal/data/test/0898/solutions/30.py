n, m = list(map(int,input().split()))

res = 1
num = int(m ** 0.5) + 1
for i in range(1, num):
    if m % i != 0:continue 
    j = m // i
    if i >= n:
        res = max(j, res)
    if j >= n:
        res = max(i, res)
print(res)

