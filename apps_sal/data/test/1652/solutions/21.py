ar = list(input())
l = len(ar)
if l < 5:
    print('NO')
else:
    while True:
        if l == 0:
            print("YES")
            return
        if "".join(ar[l-5:l]) == 'dream' or "".join(ar[l-5:l]) == 'erase':
            l -= 5
        elif "".join(ar[l-6:l]) == 'eraser':
            l -= 6
        elif "".join(ar[l-7:l]) == 'dreamer':
            l -= 7
        else:
            print("NO")
            return

