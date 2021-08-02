s = input()
q = int(input())
rev = False
top = ''
for i in range(q):
    query = input().split()

    if query[0] == '1':
        rev = not rev
    else:

        if query[1] == '1':
            if rev:
                s += query[2]
            else:
                top += query[2]
        elif query[1] == '2':
            if rev:
                top += query[2]
            else:
                s += query[2]
if rev:
    s = s[::-1] + top
else:
    s = top[::-1] + s
print(s)
