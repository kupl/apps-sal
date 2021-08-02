n, k = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]

l.sort()
l = l[n // 2:]


while k != 0:
    mini = l[0]
    compte = l.count(mini)
    if compte == len(l):
        reste = k // len(l)
        l[0] += reste
        k = 0
        break
    deux_mini = l[compte]
    diff = deux_mini - mini
    if k >= diff * compte:
        k -= diff * compte
        for i in range(compte):
            l[i] = deux_mini
    else:
        reste = k // compte
        l[0] += reste
        k = 0
        break

print(l[0])
