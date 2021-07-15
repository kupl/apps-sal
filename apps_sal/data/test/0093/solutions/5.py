a = input().strip() + input().strip()[::-1]
b = input().strip() + input().strip()[::-1]
a = a.replace("X", "")
b = b.replace("X", "")
if (a == b or a[1:] + a[:1] == b or a[2:] + a[:2] == b):
    print("YES")
else:
    print("NO")

