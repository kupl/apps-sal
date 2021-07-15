from itertools import accumulate

n = int(input())
S = {'D': (0, -1), 'U': (0, 1), 'R': (1, 0), 'L':(-1, 0)}
line = [S[c] for c in input()]
prefix_x = list(accumulate([0] + line, lambda p, q: p + q[0]))
prefix_y = list(accumulate([0] + line, lambda p, q: p + q[1]))
ans = 0
for i in range(n+1):
    for j in range(i+1, n+1):
        if prefix_x[j] == prefix_x[i] and prefix_y[j] == prefix_y[i]:
            ans += 1
print(ans)
    

