a = input()
b = input()
c = 0
for i in range(len(a)):
    if b[i:len(a)] + b[0:i] == a:
        print('Yes')
        break
    else:
        c += 1
if c == len(a):
    print('No')
