def fit(s1, s2, i):
    count = 0
    for j in range(len(s1)):
        if(s2[j + i] != s1[j]):
            if(s1[j] == '?' or s2[j + i] == '?'):
                continue
            count += 1
    return count


def calc(s1, s2, mmin):
    l = []
    for i in range(len(s1)):
        if(s1[i] != s2[i + mmin]):
            if(s1[i] == '?' or s2[i + mmin] == '?'):
                continue
            l.append(i + 1)

    return l


inp = input().split()
s1 = input()
s2 = input()
m = 9999999
mmin = 0
for i in range(len(s2) - len(s1) + 1):
    val = fit(s1, s2, i)
    if(val < m):
        m = val
        mmin = i
print(m)
l = calc(s1, s2, mmin)
for val in l:
    print(val, end=" ")

print()
