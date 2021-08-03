t = int(input())
for ii in range(t):
    a = input()
    num1, num2, num = 0, 0, 0
    ans = set()
    i = -1
    while 1:
        if i >= len(a) - 1:
            break
        i = a.find("one", i + 1)
        if i == -1:
            break
        if i > 0 and a[i - 1] == 'o':
            ans.add(i + 1)
        else:
            ans.add(i)
    i = -1
    while 1:
        if i >= len(a) - 1:
            break
        i = a.find("two", i + 1)
        if i == -1:
            break
        if i < len(a) - 3 and a[i + 3] == 'o':
            ans.add(i + 1)
        else:
            ans.add(i + 2)
    print(len(ans))
    for i in ans:
        print(i + 1, end=' ')
    print()
