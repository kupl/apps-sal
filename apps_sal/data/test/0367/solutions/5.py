x = "abcdefghijklmnopqrstuvwxyz"
d = dict.fromkeys(x, 0)
s = input()
for i in s:
    d[i] += 1
count = 0
for i in x:
    if d[i] % 2:
        count += 1
if len(s) % 2:
    count -= 1
i = len(x) - 1
while count > 0:
    if d[x[i]] % 2:
        j = 0
        while not (d[x[j]] % 2):
            j += 1
        d[x[j]] += 1
        d[x[i]] -= 1
        count -= 2
    i -= 1
s = ""
flag = ""
for i in x:
    if d[i] % 2:
        flag = i
    s += i * (d[i] // 2)
print(s, flag, s[-1::-1], sep = "")
    

