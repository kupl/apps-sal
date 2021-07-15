n = int(input())
s = input()
ss = s[:2]
s = s[2:]
for x in s:
    if ss[-2:] + x == 'fox':
        ss = ss[:-2]
    else:
        ss += x

print(len(ss))
