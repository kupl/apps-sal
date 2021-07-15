from collections import defaultdict

def isValid(n, m, freq, found):
    f = (n - 1)//m
    if f != (n - 1)/m:
        return 0
    flag = 0
    for i in found:
        if freq[i] != 0:
            if flag == 0 and freq[i] == f or freq[i] == f + 1:
                if freq[i] == f + 1:
                    flag = 1
            elif flag == 1 and freq[i] == f:
                continue
            else:
                return 0
    if flag == 0:
        return 0
    return 1

def isValid2(n, m, freq, found):
    f = (n - 1)//(m - 1)
    if f != (n - 1)/(m - 1):
        return 0
    flag = 0
    for i in found:
        if freq[i] != 0:
            if flag == 0 and freq[i] == f or freq[i] == 1:
                if freq[i] == 1:
                    flag = 1
            elif flag == 1 and freq[i] == f:
                continue
            else:
                return 0
    if flag == 0:
        return 0
    return 1

n = int(input())
freq = {}
freq = defaultdict(lambda: 0, freq)
a = list(map(int, input().split()))
m = len(set(a))
found = []
#calculation of freq
for i in a:
    freq[i] += 1
    found.append(i)
# print(freq)
found = list(set(found))
# print(found)
for i in range(n - 1, -1, -1):
    if isValid(i + 1, m, freq, found) == 0 and isValid2(i + 1, m, freq, found) == 0:
        freq[a[i]] -= 1
        if freq[a[i]] == 0:
            m -= 1
    else:
        # print(isValid(i + 1, m, freq))
        # print(isValid2(i + 1, m, freq))
        print(i + 1)
        break
