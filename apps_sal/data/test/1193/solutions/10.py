(n, k) = map(int, input().split())
s = list(map(int, input().split()))
s = list(sorted(s))
print(min(s[n - k:]))
