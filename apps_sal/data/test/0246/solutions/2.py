def sum_dig(num):
    num = str(num)
    ans = 0
    for i in range(len(num)):
        ans += int(num[i])
    return ans


(n, s) = list(map(int, input().split()))
ans = 0
for i in range(s, n + 1):
    if i - sum_dig(i) >= s:
        ans = n - i + 1
        break
print(ans)
