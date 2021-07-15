n = int(input())
s = str(n)
if s[-1] == '0':
    print(n)
else:
    n1 = n - int((s[-1]))
    n2 = n1 + 10
    if n - n1 <= n2 - n:
        print(n1)
    else:
        print(n2)
