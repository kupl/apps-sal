ans = 0
[n, h] = [int(i) for i in input().split()]
arr = [[int(i) for i in input().split()] for j in range(n)]
(l, r, answer, cur) = (0, 0, arr[0][1] - arr[0][0], 0)
arr += [[10 ** 16, 10 ** 16]]
n += 1
while r < n - 1:
    for j in range(r + 1, n):
        if cur + arr[j][0] - arr[j - 1][1] < h:
            r += 1
            cur += arr[j][0] - arr[j - 1][1]
            answer += arr[j][1] - arr[j][0]
        else:
            l += 1
            ans = max(ans, answer)
            cur -= arr[l][0] - arr[l - 1][1]
            answer -= arr[l - 1][1] - arr[l - 1][0]
            break
print(ans + h)
