n = int(input())
if n >= 0:
    print(n)
else:
    n1 = list(str(n))
    n1.pop(len(n1)-1)
    n1 = int(''.join(n1))
    n2 = list(str(n))
    n2.pop(len(n2)-2);
    n2 = int(''.join(n2))
    print(max(n1,n2))
