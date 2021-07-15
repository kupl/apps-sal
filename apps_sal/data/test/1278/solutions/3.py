n,x,y = list(map(int, input().split()))
a = list(map(int, input().split()))

for i in range(n):
    ans = True
    for j in range(i-x, i):
        if j >= 0 and a[j] < a[i]:
            ans = False
            break
    for j in range(i+1, i+y+1):
        if j < n and a[j] < a[i]:
            ans = False
            break
    if ans:
        print(i+1)
        return

