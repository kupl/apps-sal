n = int(input())
a = list(map(int,input().split()))

count = 0
while True:
    flg = False
    for i in range(n):
        if a[i] % 2 != 0:
            flg = True
    if flg:
        break
    
    for j in range(n):
        a[j] /= 2
    count += 1
print(count)
