# codeforces_1006_B
n, k = [int(e) for e in input().split(" ")]
L = [int(e) for e in input().split(" ")]
M = L[:]
M.sort()
M = M[-1:-k - 1:-1]
cursor = 0
print(sum(M))
for e in L:
    cursor += 1
    if e in M:
        M.remove(e)
        if M != []:
            print(cursor, end=" ")
            cursor = 0
        else:
            pass;
print(cursor)
