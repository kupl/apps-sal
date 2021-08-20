(n, k) = map(int, input().split())
s = input()
ans = s[:k - 1] + chr(ord(s[k - 1]) + 32) + s[k:]
print(ans)
