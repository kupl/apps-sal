t = int(input())
mass = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
flag = 1
for i in range(t):
    if arr[i] == 1 or brr[i] == 1:
        flag = 0
        break
if flag:
    ans = mass * brr[0] / (brr[0] - 1)
    for i in range(t - 1, 0, -1):
        ans = ans * arr[i] / (arr[i] - 1)
        ans = ans * brr[i] / (brr[i] - 1)
    ans = ans * arr[0] / (arr[0] - 1)
    print(ans - mass)
else:
    print("-1")
