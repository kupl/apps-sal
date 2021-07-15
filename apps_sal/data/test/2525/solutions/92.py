S = input()
Q = int(input())

lS = ''
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        lS, S = S, lS
    else:
        if query[1] == '1':
            lS += query[2]
        else:
            S += query[2]

print(lS[::-1] + S)
