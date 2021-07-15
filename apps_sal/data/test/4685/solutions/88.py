a, b, c = map(int, input().split())
k = int(input())
x = max(a, b, c)
if x == a:
    print(a*2**k + b + c)
elif x == b:
    print(a + b*2**k + c)
else:
    print(a + b + c*2**k)
