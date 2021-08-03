n, a = map(int, input().split(" "))
if a != 100:
    print(100 ** n * a)
else:
    print(100 ** n * (a + 1))
