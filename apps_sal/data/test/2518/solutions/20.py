n, a, b = map(int, input().split())
c = a-b
h = sorted([int(input()) for _i in range(n)], reverse=True)
left, right = 0, 10**9
while left < right:
    middle = (left+right)//2
    counter = 0
    checker = middle*b
    i = 0
    while checker < h[i]:
        counter -= (-h[i]+checker)//c
        i += 1
        if i >= n:
            break
    if counter <= middle:
        right = middle
    else:
        left = middle + 1
print(right)
