n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
ans = arr[0] // k
val = arr[0] % k
for i in range(1, n):
    if(val == 0):
        ans += arr[i] // k
        val = arr[i] % k
    else:
        val += arr[i]
        if(val < k):
            val = 0
            ans += 1
        else:
            ans += val // k
            val = val % k
if(val != 0):
    ans += 1
print(ans)
