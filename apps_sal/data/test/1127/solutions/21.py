def a(l):
    odd = 0
    even = 0
    for x in l:
        if x % 2 == 1:
            odd += 1
        else:
            even += 1
    return (odd, even)


T = int(input())
for _ in range(T):
    n = int(input())
    l = list(map(int, list(input())))
    odds = l[::2]
    evens = l[1::2]
    if n % 2 == 1:
        x, y = a(odds)
        print(1 if x > 0 else 2)
    else:
        x, y = a(evens)
        print(2 if y > 0 else 1)
