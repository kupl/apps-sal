n = int(input())
a = list(map(int, input().split()))
k = 0
flag = False
for i in range(n):
    if a[i] == 1 and flag == False:
        k += 1
        if i + 1 < n:
            if a[i + 1] == 0:
                flag = True
    if a[i] == 0 and flag == True:
        k += 1
        flag = False
if a[-1] == 0:
    k -= 1
if k < 0:
    print(0)
else:
    print(k)
