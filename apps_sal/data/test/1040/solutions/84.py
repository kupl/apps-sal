n = int(input())
s = input()
q = ''
sub = 0
for i in s:
    q += i
    if len(q) >= 3 and q[-3:] == 'fox':
        sub += 3
        q = q[:-3]
print(n - sub)
