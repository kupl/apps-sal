h, w, k = map(int, input().split(' '))
c = [input() for x in range(h)]
cnt = 0

for maskR in range(2**h):
    for maskC in range(2**w):
        black = 0
        for i in range(h):
            for j in range(w):
                if (((maskR >> i) &1) == 0
                    and ((maskC >> j) &1) == 0 and c[i][j] == '#'):
                    black += 1
        if black == k:
            cnt += 1
print(cnt)
