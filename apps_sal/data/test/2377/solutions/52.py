import sys

N, H = map(int, sys.stdin.readline().split())

katanas = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    katanas.append((a, b, i))

sk = sorted(katanas, reverse=True)
max_k = sk[0][0]

katanas.sort(key = lambda x:x[1], reverse=True)
ans = 0
i = 0
while H > 0:
    if i < N and katanas[i][1] > max_k:
        H -= katanas[i][1]
        i += 1
        ans += 1
    else:
        tmp = (H - 1) // max_k + 1
        H -= tmp * max_k
        ans += tmp
        
print(ans)
