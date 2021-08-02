def main():
    tmp = input()
    tmp = tmp.split(" ")
    n = int(tmp[0])
    l = int(tmp[1])
    tmp = input()
    tmp = tmp.split(" ")
    a = []
    for i in tmp:
        a.append(int(i))
    tmp = input()
    tmp = tmp.split(" ")
    b = []
    for i in tmp:
        b.append(int(i))
    a1 = []
    for i in range(1, len(a)):
        a1.append(a[i] - a[i - 1])
    a1.append(l - a[-1] + a[0])
    b1 = []
    for i in range(1, len(b)):
        b1.append(b[i] - b[i - 1])
    b1.append(l - b[-1] + b[0])
    tmp = len(a1)
    for i in range(tmp):
        lol = a1[0]
        a1.pop(0)
        a1.append(lol)
        if (a1 == b1):
            print("YES")
            return 0
    print("NO")


main()
