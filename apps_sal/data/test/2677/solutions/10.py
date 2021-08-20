v = ['a', 'e', 'i', 'o', 'u']
c = []
vo = 0
co = 0
k = []
p = []
for i in range(97, 123):
    if chr(i) not in v:
        c = c + [chr(i)]
x = input().lower()
for i in range(len(x)):
    if x[i] in v:
        vo += 1
    else:
        p = p + [vo]
        vo = 0
    if x[i] in c:
        k = k + [x[i]]
k = list(set(k))
p = list(filter(lambda x: x >= 3, p))
if len(p) >= 1 and len(k) >= 5:
    print('GOOD')
else:
    print(-1)
