(n, k) = map(int, input().split())
s = input()
s = s[k - 1:] + s[:k - 1]
ans = s.capitalize().swapcase()
print(ans[n - k + 1:] + ans[:n - k + 1])
