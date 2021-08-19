n = input()
f = 0
for i in range(0, len(n)):
    if n[i] == '7':
        print('Yes')
        f = 1
        break
if f == 0:
    print('No')
