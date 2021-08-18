n = int(input())
arr = ["."] * n
d = dict()
for i in range(n):
    arr[i] = input().strip()
    s = set()
    for j in range(len(arr[i])):
        s.add(arr[i][j])
    if len(s) <= 2:
        try:
            d[arr[i]][0] += 1
        except:
            d[arr[i]] = [1, s]
ans = 0
for i in range(97, 97 + 26):
    for j in range(97, 97 + 26):
        c = 0
        a, b = chr(i), chr(j)
        q = set([a, b])
        for k in list(d.keys()):
            if q >= d[k][1]:
                c += d[k][0] * len(k)
        ans = max(ans, c)
print(ans)
