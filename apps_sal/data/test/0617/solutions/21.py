s = input()
s = "0+1*" + s + "*1+0"
answer = eval(s)
n = len(s)
p = []
for i in range(0, n):
    if s[i] == '*':
        p.append(i)
for i in p:
    for j in p:
        if i >= j:
            continue
        test = eval(s[:i + 1] + "(" + s[i + 1:j] + ")" + s[j:])
        if test > answer:
            answer = test
print(answer)
