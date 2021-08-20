(n, ones, twos) = list(map(int, input().split()))
semi = 0
deny = 0
humans = list(map(int, input().split()))
for k in humans:
    if k == 1:
        if ones > 0:
            ones -= 1
        elif ones == 0:
            if twos > 0:
                twos -= 1
                semi += 1
            elif twos == 0:
                if semi > 0:
                    semi -= 1
                else:
                    deny += 1
    elif k == 2:
        if twos > 0:
            twos -= 1
        else:
            deny += 2
print(deny)
