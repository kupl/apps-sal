n = int(input())
a = input()
f = [int(x) for x in input().split()]
r = ''
flag = -1
for c in a:
    k = f[int(c) - 1]
    if flag == -1:
        if k > int(c):
            flag = 0
            r += str(k)
        else:
            r += c
    elif flag == 0:
        if k < int(c):
            r += c
            flag = 1
        else:
            r += str(k)
    else:
        r += c
print(r)
