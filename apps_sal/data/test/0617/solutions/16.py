s = input()
d = list(s.split('*'))
last = 0
po = []
ki = []
for i in range(len(d)):
    po += [last]
    ki += [len(d[i]) + last]
    last += len(d[i]) + 1
ans = [eval(s)]
for a in po:
    for b in ki:
        if a > b - 2:
            continue
        x = s[:a] + '(' + s[a:b] + ')' + s[b:]
        ans += [eval(x)]
print(max(ans))
