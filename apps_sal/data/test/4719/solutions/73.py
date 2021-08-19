n = int(input())
words = []
for i in range(n):
    words.append(input())
s = words.pop()
for i in words:
    ns = ''
    l = list(i)
    for j in s:
        if j in l:
            ns += j
            l.remove(j)
    s = ns
s = sorted(list(s))
out = ''
for i in s:
    out += i
print(out)
