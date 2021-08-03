t = 1
i = 1
l = int(input())
while l:
    if t < i / sum(map(int, list(str(i)))):
        i += 9 * t
        t *= 10
    else:
        print(i)
        i += t
        l -= 1
