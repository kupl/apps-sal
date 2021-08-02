n, k = list(map(int, input().split()))
s = input()

print((s[:k - 1] + chr(ord(s[k - 1]) + 32) + s[k:]))
