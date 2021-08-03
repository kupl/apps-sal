n = int(input())
s = [int(input()) for i in range(n)]
s.sort()
S = sum(s)
ans = 0
if S % 10 != 0:
    print(S)
else:
    for i in range(n):
        if (S - s[i]) % 10 != 0:
            ans = max(S - s[i], ans)
    print(ans)
