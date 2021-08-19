(n, k) = list(map(int, input().split()))
v = list(map(int, input().split()))
ans = 0
for left in range(min(n, k + 1)):
    for right in range(min(n - left + 1, k - left + 1)):
        l = v[:left]
        l += v[::-1][:right]
        l.sort()
        temp = sum(l)
        for t in range(max(0, min(len(l), k - left - right))):
            if l[t] < 0:
                temp -= l[t]
        ans = max(ans, temp)
print(ans)
