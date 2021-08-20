(n, q) = list(map(int, input().split()))
s = input()
ls = [list(map(int, input().split())) for i in range(q)]
d = [0]
pre = 0
c = 0
for i in range(len(s) - 1):
    if s[i:i + 2] == 'AC':
        d.append(d[i] + 1)
    else:
        d.append(d[i])
for (start, end) in ls:
    print(d[end - 1] - d[start - 1])
