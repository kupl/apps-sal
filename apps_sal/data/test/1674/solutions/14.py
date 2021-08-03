n, k = map(int, input().split())
a = list(map(int, input().split()))
s = input()
ans = 0
now = []
now.append(a[0])
for i in range(1, n):
    if s[i] == s[i - 1]:
        now.append(a[i])
    else:
        if len(now) > k:
            now.sort(key=lambda x: -x)
            ans += sum(now[:k])
        else:
            ans += sum(now)
        now = [a[i]]
if len(now) > k:
    now.sort(key=lambda x: -x)
    ans += sum(now[:k])
else:
    ans += sum(now)
now = []
print(ans)
