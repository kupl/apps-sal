s = input()
q = int(input())
head = ''
tail = ''
rev = 0

for _ in range(q):
    T = list(input().split())
    if T[0] == '1':
        head, tail = tail, head
        rev += 1
    else:
        if T[1] == '1':
            head += T[2]
        else:
            tail += T[2]

if rev%2 == 0:
    print((head[::-1]+s+tail))
else:
    print((head[::-1]+s[::-1]+tail))

