a = list(input())
b = list(input())
c = list(input())
ans = 'a'
while True:
    try:
        if ans == 'a':
            ans = a[0]
            a = a[1:]
        elif ans == 'b':
            ans = b[0]
            b = b[1:]
        elif ans == 'c':
            ans = c[0]
            c = c[1:]
    except:
        print(ans.upper())
        break
