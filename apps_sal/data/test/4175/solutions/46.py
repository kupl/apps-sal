n = int(input())
s = input()
ws = set()
ws.add(s)
last = s[-1]
for _ in range(n-1):
    s = input()
    if s in ws or s[0] != last:
        print('No')
        break
    else:
        ws.add(s)
        last = s[-1]
else:
    print('Yes')
