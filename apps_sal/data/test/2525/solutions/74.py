s = input()
q = int(input())

h = 0
t = ''
b = ''

for i in range(q):
    x = list(input().split())

    if len(x) == 1:
        h += 1

    elif h % 2 == 0:
        if x[1] == '1':
            t = (x[-1]) + t
        else:
            b += (x[-1])

    elif h % 2 == 1:
        if x[1] == '1':
            b += (x[-1])
        else:
            t = (x[-1]) + t

if h % 2 == 0:
    print(t + s + b)

else:
    s = t + s + b
    s = s[::-1]
    print(s)
