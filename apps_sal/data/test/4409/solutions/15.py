def solve(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    m = 0
    elem = 0
    for i in d:
        if d[i] > m:
            m = d[i]
            elem = i
    print(len(a) - m)
    start = -1
    for i in range(len(a)):
        if a[i] == elem:
            start = i
            break
    for i in range(start - 1, -1, -1):
        if a[i] < elem:
            print('1 ' + str(i + 1) + ' ' + str(i + 2))
        else:
            print('2 ' + str(i + 1) + ' ' + str(i + 2))
    for i in range(start + 1, len(a)):
        if a[i] != elem:
            if a[i] < elem:
                print('1 ' + str(i + 1) + ' ' + str(i))
            else:
                print('2 ' + str(i + 1) + ' ' + str(i))


n = int(input())
x = input().split()
a = []
for i in x:
    a.append(int(i))
solve(a)
