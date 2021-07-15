n, m, k = list(map(int,input().split()))
p = list(map(int,input().split()))
s = list(map(int,input().split()))
c = list(map(int,input().split()))

dct = {}
for i in range(n):
    if s[i] in dct:
        dct[s[i]] = max(dct[s[i]], p[i])
    else:
        dct[s[i]] = p[i]


data_to_fuck_you = 0
for i in range(k):
    power = p[c[i] - 1]
    school = s[c[i] - 1]

    if power < dct[school]:
        data_to_fuck_you += 1

print(data_to_fuck_you)


