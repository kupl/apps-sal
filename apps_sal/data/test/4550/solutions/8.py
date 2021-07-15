# A+B=C か　A+C=B か B+C=Aになるか判定

a, b, c = map(int, input().split())
if a + b == c or a + c == b or b + c == a:
    print('Yes')
else:
    print('No')
