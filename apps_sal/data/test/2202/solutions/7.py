n, m = map(int, input().split())
arr = list(map(int, input().split()))
s1 = arr[0]
s2 = sum(arr) - arr[0]
ans = [s1 % m + s2 % m]
for i in range(1, n - 1):
    s1 += arr[i]
    s2 -= arr[i]
    ans.append(s1 % m + s2 % m)
print(max(ans))
