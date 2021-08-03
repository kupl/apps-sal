n = int(input())
arr = [int(i) for i in input().split()]
ans = 1e10
for i in range(len(arr)):
    if i != 0:
        sub1 = min(arr[i], arr[0]) // i
    else:
        sub1 = 1e10
    if i != n - 1:
        sub2 = min(arr[i], arr[-1]) // (n - 1 - i)
    else:
        sub2 = 1e10
    ans = min(ans, sub1, sub2)
print(ans)
