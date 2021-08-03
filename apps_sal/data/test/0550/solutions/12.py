log = input()
log = log.lower()
log = log.replace('0', 'o')
log = log.replace('i', '1')
log = log.replace('l', '1')
a = int(input())
logs = set()
for i in range(a):
    s = input()
    s = s.lower()
    s = s.replace('0', 'o')
    s = s.replace('i', '1')
    s = s.replace('l', '1')
    logs.add(s)
if log in logs:
    print('No')
else:
    print('Yes')
