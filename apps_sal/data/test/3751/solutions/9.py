A = "abcdefghijklmnopqrstuvwxyz"

s = input()

was = set()

s2 = ""

for c in s:
    if c not in was:
        s2 += c
        was.add(c)

print("YES" if A.startswith(s2) else "NO")
