N = int(input())
s = input()
ps = ''
for c in s:
    ps += c
    if ps[len(ps) - 3:len(ps)] == 'fox':
        ps = ps[0:len(ps) - 3]
print(len(ps))
