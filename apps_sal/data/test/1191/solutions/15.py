n, k = input().split(' ')
n = int(n)
k = int(k)
power2 = input().split(' ')
gold = input().split(' ')
prof = [0] * k
sums = dict()
s = 0
d = dict()
for i in range(n):
    power2[i] = int(power2[i])
    gold[i] = int(gold[i])
    d[power2[i]] = gold[i]
power = sorted(power2)
for i in range(n):
    ind = power[i]
    coin = d[ind]
    for j in range(k):
        if prof[j] >= coin:
            sums[ind] = s + coin
            prof.insert(j, coin)
            s = s - prof[0] + coin
            del prof[0]
            break
    else:
        sums[ind] = s + coin
        prof.append(coin)
        s = s - prof[0] + coin
        del prof[0]
st = ''
for elem in power2:
    st += str(sums[elem]) + ' '
print(st)
