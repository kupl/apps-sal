s = input()
p = int(s.split()[0])
n = int(s.split()[1])
nn = []
bb = False
for i in range(n):
    a = int(input()) % p
    for b in nn:
        if b == a:
            print(i + 1)
            bb = True
            break
    else:
        nn.append(a)
    if bb:
        break
if not bb:
    print(-1)
