a = input()
b = input()
ans = 0
pos = a.find(b)
while pos != -1:
    a = a[pos + len(b):]
    ans += 1
    pos = a.find(b)
print(ans)
