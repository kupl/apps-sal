n = int(input())
a = list(map(int, input().split()))
b = []
p = -1
for e in a:
    if e == p:
        continue
    else:
        b.append(e)
        p = e

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    x, y = len(a), len(b)
    return lengths[x][y]

ans = 0

#print(b)
#for i in range(len(b)//2+1):
    #print(list(reversed(b[:i])), b[i:])
    #ans = max(ans, lcs(list(reversed(b[:i])), b[i:]))

ans = lcs(list(reversed(b)), b)//2
n = len(b)
#print(ans)
print(n - ans - 1)
