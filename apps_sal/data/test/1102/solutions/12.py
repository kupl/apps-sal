(n, a) = map(int, input().split())
t = list(map(int, input().split()))
cnt = [0 for i in range(101)]
crime = [0 for i in range(101)]
for i in range(1, n + 1):
    d = abs(a - i)
    cnt[d] += 1
    crime[d] += t[i - 1]
ans = 0
for i in range(101):
    if crime[i] == cnt[i]:
        ans += crime[i]
print(ans)
