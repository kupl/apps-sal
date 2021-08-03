n = int(input())
x = list(map(int, input().split()))
e = n
my = set()
for i in range(0, n):
    my.add(x[i])
    if x[i] == e:
        while e in my:
            print(e, end=' ')
            my.remove(e)
            e = e - 1
        print()
    else:
        print()
