N = int(input())
S = list(input())
L = [chr(x) for i in range(2) for x in range(65, 65 + 26)]

for s in S:
    ind = L.index(s)
    print(L[ind + N], end="")

print("")
