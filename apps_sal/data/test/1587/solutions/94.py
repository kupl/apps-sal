n = int(input())
C = input()
r_all = C.count('R')
move = [0] * (n + 1)
w = 0
r = r_all
move[0] = max(0, r_all)
for (idx, c) in enumerate(C):
    if c == 'W':
        w += 1
    else:
        r -= 1
    move[idx + 1] = max(w, r)
ans = min(move)
print(ans)
