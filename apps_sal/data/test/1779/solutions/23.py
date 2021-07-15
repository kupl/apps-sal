d = dict()
tr = dict()
alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
for i in range(26):
    tr[alpha[2 * i + 1]] = alpha[2 * i]
r1 = input()
r2 = input()
for s in range(26):
    d[r1[s]] = r2[s]
    d[tr[r1[s]]] = tr[r2[s]]
text = input()
ans = ''
for i in text:
    if i in d.keys():
        ans += d[i]
    else:
        ans += i
print(ans)
