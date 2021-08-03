Q = set()
T = input()
for P in range(len(T) + 1):
    for L in range(26):
        Q.add(T[:P] + str(chr(L + 97)) + T[P:])
print(len(Q))
