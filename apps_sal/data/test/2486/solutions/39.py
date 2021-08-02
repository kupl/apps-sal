n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = n
s, cnt = 0, 0
for i in a:
    cnt += 1
    if s + i < k:
        s += i
    else:
        ans = n - cnt
print(ans)
