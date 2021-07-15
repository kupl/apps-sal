n,d = map(int,input().split())
a = 2 * d + 1
if n % a == 0:
    print(n // a)
else:
    print(n // a + 1)
