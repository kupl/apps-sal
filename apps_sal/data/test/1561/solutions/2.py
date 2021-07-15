n, m, k = list(map(int, input().split()))

result = 0

M1 = []
for _ in range(n):
    M1.append(list([x == '*' for x in input()]))

M2 = [[M1[j][i] for j in range(n)] for i in range(m)]

#print(M2)

for M in ([M1, M2] if k > 1 else [M1]):
    for row in M:
        cnts = []
        sofar = 0
        for seat in row:
            if not seat:
                sofar += 1
            else:
                cnts.append(sofar)
                sofar = 0
        cnts.append(sofar)
        #print(cnts)

        for cnt in cnts:
            result += max(0, cnt-k+1)

print(result)

