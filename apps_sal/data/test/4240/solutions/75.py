import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
s = lines.pop(0)
t = lines.pop(0)
for i in range(len(s)):
    if s[i:] + s[:i] == t:
        print("Yes")
        break
else:
    print("No")
