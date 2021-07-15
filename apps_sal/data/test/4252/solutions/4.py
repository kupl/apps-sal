n = int(input())

niz = input().strip()

count = 0
i = 0
while i+2 < len(niz):
    if niz[i:i+3] == 'xxx':
        niz = niz[:i+2] + niz[i+3:]
        count += 1
        i = 0
    else:
        i += 1

print(count)

