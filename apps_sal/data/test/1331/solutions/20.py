(n, m, k) = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
size = k - 1
ans = []
f = 0
i = 0
while i < n:
    if ans == []:
        if len(ans) < size:
            ans.append(arr[i])
            i += 1
        else:
            f += 1
            i += 1
    else:
        u = ans[0]
        limit = u + m - 1
        while i < n:
            if arr[i] <= limit:
                if len(ans) < k - 1:
                    ans.append(arr[i])
                else:
                    f += 1
                i += 1
            else:
                break
        ans.pop(0)
print(f)
