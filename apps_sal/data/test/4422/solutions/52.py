(n, k) = map(int, input().split())
s = list(input())
ss = s[k - 1]
p = ss.lower()
s[k - 1] = p
ans = ''.join(s)
print(ans)
