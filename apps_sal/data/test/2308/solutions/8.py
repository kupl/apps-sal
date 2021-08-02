t = int(input())
for _ in range(t):
    x = input()
    y = input()
    lst = len(y) - y.rfind('1')
    out = False
    for i in range(lst, len(x) + 1):
        if x[-i] == '1':
            print(i - lst)
            out = True
            break
    if out:
        continue
