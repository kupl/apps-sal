
import sys
# sys.stdin=open("data.txt")
input = sys.stdin.readline

g = [list(input().strip()) for _ in range(10)]

ans = 0

for i in range(10):
    for j in range(10):
        if g[i][j] != '.': continue
        g[i][j] = 'X'
        # check possible
        for p in range(10):
            for q in range(10):
                # cancer
                if p + 4 < 10:
                    cnt = 0
                    for r in range(5):
                        if g[p + r][q] == 'X':
                            cnt += 1
                    if cnt == 5: ans = 1
                if q + 4 < 10:
                    cnt = 0
                    for r in range(5):
                        if g[p][q + r] == 'X':
                            cnt += 1
                    if cnt == 5: ans = 1
                if p + 4 < 10 and q + 4 < 10:
                    cnt = 0
                    for r in range(5):
                        if g[p + r][q + r] == 'X':
                            cnt += 1
                    if cnt == 5: ans = 1
                    cnt = 0
                    for r in range(5):
                        if g[p + 4 - r][q + r] == 'X':
                            cnt += 1
                    if cnt == 5: ans = 1
        # done
        g[i][j] = '.'

print("YES" if ans else "NO")
