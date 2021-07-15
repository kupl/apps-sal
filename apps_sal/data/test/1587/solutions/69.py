N = int(input())
c = input()
w = 0
r = c.count('R')
Cand ={r}
for i in range(N):
    if c[i] == 'R':
        r -= 1
    else:
        w += 1
    Cand.add(max(w,r))
print(min(Cand))
