3

s = input()

mx = -1
for c in s:
    if ord(c) > ord('a') + mx + 1:
        print("NO")
        return
    else:
        mx = max(mx, ord(c) - ord("a"))

print("YES")

