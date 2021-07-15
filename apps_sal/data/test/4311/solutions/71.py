s = int(input())
a = [s]
while True:
    if s % 2 == 0:
        s = s // 2
    else:
        s = s * 3 + 1
    a.append(s)
    if a.count(s) == 2:
        print(len(a))
        break
