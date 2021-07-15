n = int(input())
lst = list(map(int,input().split()))
ans = 0
for i in range(n - 1):
    if (lst[i] > lst[i + 1]):
        lst[i + 1] = lst[i + 1] + 1
    if (lst[i] > lst[i + 1]):
        ans = 1

if(ans == 0):
    print("Yes")
else:
    print("No")
