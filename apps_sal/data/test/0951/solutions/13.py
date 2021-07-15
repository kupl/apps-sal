from sys import stdin, stdout


k = int(stdin.readline().rstrip())
n = stdin.readline().rstrip()

n = sorted(n)

ck = 0
for c in n:
    ck += ord(c) - ord('0')

if ck >= k:
    print(0)
else:
    rez = 0
    for c in n:
        ck += ord('9') - ord(c)
        rez += 1
        if ck >= k:
            print(rez)
            break
