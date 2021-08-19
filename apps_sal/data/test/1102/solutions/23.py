(n, a) = map(int, input().split())
arr = list(map(int, input().split()))
a -= 1
ans = 0
for i in range(n):
    if i == a:
        ans += arr[i]
    elif i < a:
        j = 2 * a - i
        if j >= n or arr[j] == 1:
            ans += arr[i]
    else:
        j = 2 * a - i
        if j < 0 or arr[j] == 1:
            ans += arr[i]
print(ans)
