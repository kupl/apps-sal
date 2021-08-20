n = int(input())
s = str(n)
m = int(max(s))
print(m)
for i in range(m):
    ed = False
    for j in range(len(s)):
        if int(s[j]) > i:
            ed = True
            print(1, end='')
        elif ed:
            print(0, end='')
    print(' ', end='')
