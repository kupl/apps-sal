a = input()
b = input()
ans = 0
pos = a.find(b)
while pos != -1:
    # tmp = b.replace(b[0], '#', 1)
    a = a[(pos + len(b)):]
    ans += 1
    # print(a)
    pos = a.find(b)
print(ans)
