s = list(input())
l = len(s)
if l % 2 == 0:
    for i in range(l//2):
        a = s[l//2]
        if s[l//2 - 1 - i] != a or s[l//2 + i] != a:
            print(l//2 + i)
            return
else:
    for i in range(1, (l-1)//2 + 1):
        a = s[(l-1)//2]
        if s[(l-1)//2 - i] != a or s[(l-1)//2 + i] != a:
            print((l-1)//2 + i)
            return
print(l)
