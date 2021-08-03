n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
ans = []
for i in range(1, n + 1):
    for j in range(n - i + 1):
        ans.append(sum(arr[j:j + i]))
ans.sort()
ans
print(str(list(reversed(ans[-k:]))).replace(",", "")[1:-1])
