n, p, k = [int(x) for x in input().split()]
s = ''
if p > k + 1:
    s += "<< "
for i in range(max(1, p-k), p):
    s += str(i) + ' '
s += '('+str(p)+') '
for i in range(p + 1, min(n, p+k)+1):
    s += str(i) + ' '
if p + k < n:
    s += '>>'
print(s)
