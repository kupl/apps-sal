a, b = map(int, input().split())
c = input()
clock = c.find(".")

for x in range(clock + 1, a):
    if c[x] > '4':
        break
else:
    x = a
    print(c)
if x != a:
    while b:
        x -= 1
        b -= 1
        if c[x] != '4':
            break
    if x > clock:
        print(c[:x], chr(ord(c[x]) + 1), sep="")
    else:
        c = list(c[:x])
        x -= 1
        while x >= 0:
            if c[x] == '9':
                c[x] = '0'
                x -= 1
            else:
                c[x] = chr(ord(c[x]) + 1)
                break
        else:
            c.insert(0, '1')
        print("".join(c))
