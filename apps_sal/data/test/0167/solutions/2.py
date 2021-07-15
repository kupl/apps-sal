a = input()
b = input()
p = [None] * (len(b) + 1)
s = [None] * (len(b) + 1)
j = 0
p[0] = -1
for i in range(len(b)):
    while j < len(a) and a[j] != b[i]:
        j += 1
    if j >= len(a):
        break
    else:
        p[i + 1] = j
        j += 1
j = len(a) - 1
s[-1] = len(b)
for i in range(len(b) - 1, -1, -1):
    while j >= 0 and a[j] != b[i]:
        j -= 1
    if j < 0:
        break
    else:
        s[i] = j
        j -= 1
ans = ""
for i in range(len(b) + 1):
    if p[i] == None:
        break
    else:
        l = i - 1
        r = len(b)
        while l + 1 < r:
            mid = (l + r) // 2
            if s[mid] != None and p[i] < s[mid]:
                r = mid
            else:
                l = mid
        if len(ans) < i + len(b) - r:
            ans = b[:i] + b[r:]
if ans == "":
    print("-")
else:
    print(ans)
