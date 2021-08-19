n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

ansl = []
if n != 0:
    while abs(n) > 0:
        if n % 2 == 0:
            ansl.append("0")
            n = n // (-2)
        else:
            ansl.append("1")
            n = (n - 1) // (-2)
    print((''.join(ansl[::-1])))
else:
    print((0))
