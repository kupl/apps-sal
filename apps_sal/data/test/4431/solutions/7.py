(n, k) = tuple(map(int, input().split()))
s = input() + '!'
lets = set(input().split())
ans = 0
cnt = 0
for i in s:
    if i in lets:
        cnt += 1
    else:
        ans += cnt * (cnt + 1) // 2
        cnt = 0
print(ans)
