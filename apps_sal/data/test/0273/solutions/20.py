(st1, st2) = (input().split())
d = 0
for i in st1:
    if i < st2[0] or not d:
        d = 1
        print(i, end='')
    else:
        break
print(st2[0])
