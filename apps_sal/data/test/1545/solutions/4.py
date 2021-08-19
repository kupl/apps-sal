#!/usr/bin/env python3
def ri():
    return list(map(int, input().split()))


n = int(input())
s = input()
s = [ord(x) - ord('a') for x in s]
a = list(ri())

T = [0 for i in range(n)]

maxs = 0
mins = 0
lasts = 0
for i in range(len(s)):
    if i == 0:
        maxs = 1
        T[i] = 1
        mins += 1
        continue
    mm = i
    smin = 10**9
    for j in range(i, max(i - a[s[i]], -1), -1):
        length = i - j + 1
        flag = 0
        smin = min(a[s[j]], smin)
        if smin < length:
            break
        else:
            mm = j
            if j == 0:
                adding = 1
            else:
                adding = T[j - 1]
            T[i] += adding
            T[i] = T[i] % (10**9 + 7)
    maxs = max(maxs, i - mm + 1)
    if mm > lasts:
        mins += 1
        lasts = i

print(T[n - 1])
print(maxs)
print(mins)
