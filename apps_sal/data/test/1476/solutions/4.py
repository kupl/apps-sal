n = int(input().strip())
if 2 >= n:
    print(1)
    print(1)
elif 3 == n:
    print(2)
    print('1 3')
else:
    print(n)
    sits = [1]
    place = 0
    for i in range(n, 1, -1):
        if 0 == place:
            sits.append(i)
        else:
            sits = [i] + sits
        place = (place + 1) % 2
    print(' '.join(map(str, sits)))
