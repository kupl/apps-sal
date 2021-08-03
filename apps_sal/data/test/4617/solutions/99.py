s = input()
t = input()
print("YES" if s == t[::-1] and t == s[::-1] else "NO")
