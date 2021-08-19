input()
s = input()
first = s[0]
last = s[-1]
answ = 0
if first == '<':
    for i in range(len(s)):
        if s[i] == first:
            answ += 1
        else:
            break
if last == '>':
    for i in range(len(s) - 1, -1, -1):
        if s[i] == last:
            answ += 1
        else:
            break
print(answ)
