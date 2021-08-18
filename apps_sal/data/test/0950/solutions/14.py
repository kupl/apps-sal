import string


def get_min_distance(str, alphabet):
    m = len(str)
    mi = m
    for i in range(m):
        if str[i] in alphabet:
            mi = min(i, mi)
            break
    for i in range(m):
        if str[-i] in alphabet:
            mi = min(i, mi)
            break
    return mi


n, m = map(int, input().split())
strs = []
for i in range(n):
    strs.append(input())
mins = []
for i in range(n):
    mins.append([get_min_distance(strs[i], string.digits),
                 get_min_distance(strs[i], string.ascii_lowercase),
                 get_min_distance(strs[i], "

mincost=10**6
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if j == k or i == k:
                continue
            mincost=min(mincost, mins[i][0] + mins[j][1] + mins[k][2])
print(mincost)
