import sys

next_allowed = 'a'

s = input()
for c in s:
    if ord(c) > ord(next_allowed):
        print("NO")
        return
    elif ord(c) == ord(next_allowed):
        next_allowed = chr(ord(next_allowed) + 1)

print("YES")

