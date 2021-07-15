s = input()
k = int(input())
a = list(map(int,input().split()))
ma = 1
ans = 0
for i in range(len(a)):
    if a[ma] < a[i]:
        ma = i
for i in range(len(s)):
    ans += a[ord(s[i]) - ord('a')] * (i + 1)
for i in range(len(s), len(s) + k):
    ans += a[ma] * (i + 1)
print(ans)
