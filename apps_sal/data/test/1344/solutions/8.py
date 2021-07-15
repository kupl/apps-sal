n = int(input())
a = list(map(int, input().split()))
res = 1
m = 1
for i in range(1, n):
    if  a[i] > a[i-1]:
        res +=1
    else:
        if res > m:
            m = res
        res = 1
if res > m:
    m = res
print(m)

