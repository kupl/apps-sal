s = int(input())
a = [s]
b = 1
while True:
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1
    if s in a:
        print(len(a) + 1)
        return
    a.append(s)
