n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if a[i] >= b[i]:
        cnt += b[i]
    elif a[i] < b[i] and a[i] + a[i+1] >= b[i]:
        cnt += b[i]
        a[i+1] = a[i+1] - (b[i] - a[i])
    else:
        cnt += (a[i] + a[i+1])
        a[i+1] = 0
print(cnt)
