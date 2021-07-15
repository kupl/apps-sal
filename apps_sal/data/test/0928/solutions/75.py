n,k = list(map(int,input().split()))
a = list(map(int,input().split()))

right = 0
cnt = 0
suma = 0
for left in range(n):
    while right<n and suma+a[right]<k:
        suma += a[right]
        right += 1
    cnt += n - right
    if left==right:
        right += 1
    else:
        suma -=a[left]
print(cnt)

