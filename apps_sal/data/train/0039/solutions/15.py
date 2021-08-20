t = int(input())
while t:
    t += -1
    (a, b, p) = map(int, input().split())
    s = input()
    l = []
    for i in s:
        l.append(i)
    cost = 0
    for i in range(len(l) - 1):
        if l[i + 1] != l[i]:
            if l[i] == 'A':
                cost += a
            else:
                cost += b
    if l[len(l) - 1] == l[len(l) - 2]:
        if l[len(l) - 1] == 'A':
            cost += a
        else:
            cost += b
    ind = -1
    for i in range(len(l) - 1):
        if cost <= p:
            ind = i
            break
        if l[i + 1] != l[i]:
            if l[i] == 'A':
                cost -= a
            else:
                cost -= b
    if ind == -1:
        print(len(l))
    else:
        print(ind + 1)
