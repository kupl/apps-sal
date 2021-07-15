n = int(input())
s1 = 'I hate that '
s2 = 'I love that '
s11 = 'I hate it'
s22 = 'I love it'
s =''
for i in range(n-1):
    if i % 2 == 0:
        s += s1
    else:
        s += s2
if n % 2 == 1:
    s += s11
else:
    s += s22
        
print(s )

