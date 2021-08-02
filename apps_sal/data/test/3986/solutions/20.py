n, k = map(int, input().split())
if n < k:
    print(-1)
    return
if n == k:
    ans = [chr(i + 97) for i in range(k)]
    print(''.join(ans))
    return
if k == 1:
    print(-1)
    return
if k == 2:
    ans = "ab" * (n // 2) + "ab"[:n % 2]
    print(ans)
    return
rem = k - 2
ans = "ab" * (n // 2) + "ab"[:n % 2]
ans = list(ans)
c = 99
for i in range(n - rem, n):
    ans[i] = chr(c)
    c += 1
print(''.join(ans))
