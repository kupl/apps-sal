t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    hashi = dict()
    l = input().split()
    li = [int(i) for i in l]
    maxa = []
    for i in li:
        if(i % k):
            z = k - (i % k)
            if(z in hashi):
                hashi[z] += 1
            else:
                hashi[z] = 1
    for i in hashi:
        maxa.append((hashi[i] - 1) * k + i)
    if(maxa == []):
        print(0)
        continue
    print(max(maxa) + 1)
