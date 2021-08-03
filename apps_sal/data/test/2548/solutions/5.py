t = int(input())
for you in range(t):
    n = int(input())
    l = input()
    hashi = dict()
    hashi[0] = 1
    count = 0
    sumi = 0
    for i in range(n):
        sumi = sumi + (int(l[i]))
        z = sumi - (i + 1)
        if(z in hashi):
            count = count + hashi[z]
            hashi[z] += 1
        else:
            hashi[z] = 1
    print(count)
