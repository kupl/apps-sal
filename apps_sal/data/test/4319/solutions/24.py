n = int(input())
s = list(map(int, input().split()))
x = s[0]
ans = 1
ans1 = []
for i in range(1, n):
    if s[i] != s[i - 1] + 1:
        ans += 1
        ans1.append(s[i - 1])
ans1.append(s[-1])
print(ans)
for i in ans1:
    print(i, end=' ')
