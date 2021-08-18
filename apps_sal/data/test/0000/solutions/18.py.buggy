s = input()
rev = s[::-1]

left = s.find("[")
if left != -1:
    left = s.find(":", left)

right = rev.find("]")
if right != -1:
    right = rev.find(":", right)

if left == -1 or right == -1:
    print(-1)
    return
right = len(s) - right - 1
if left >= right:
    print(-1)
    return

print(4 + s[left:right].count("|"))
