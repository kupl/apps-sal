def is_palindrome(ss):
    return ss == ss[::-1]


s = input().strip()
best = 0
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if not is_palindrome(s[i:j]):
            best = max(best, j - i)
print(best)
