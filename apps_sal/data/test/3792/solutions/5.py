(n, k) = list(map(int, input().split()))
s1 = input()
s2 = input()
cnt = 1
ans = 0
for i in range(n):
    cnt *= 2
    if s1[i] == 'b':
        cnt -= 1
    if s2[i] == 'a':
        cnt -= 1
    cnt = min(1e+18 + 7, cnt)
    ans += min(cnt, k)
print(ans)
