from sys import stdin

n = int(stdin.readline())

stones = sorted([int(x) for x in stdin.readline().split()])

if n == 1:
    if stones[0] % 2 == 0:
        print('cslnb')
    else:
        print('sjfnb')

else:
    chilly = -1
    chill = 2
    prev = stones[0]

    for x in stones[1:]:
        if x == prev:
            chill -= 1
            chilly = x
        else:
            streak = 1
            prev = x

    s = sum(stones)

    if n % 4 == 0 or n % 4 == 1:
        s += 1

    if chill <= 0 or stones.count(0) > 1:
        print('cslnb')
    elif chill == 1 and chilly - 1 in stones:
        print('cslnb')
    elif s % 2 == 1:
        print('cslnb')
    else:
        print('sjfnb')
