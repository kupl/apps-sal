from collections import defaultdict

N, X, Y = map(int, input().split())
cnt_dict = defaultdict(int)

for i in range(1,N):
    for j in range(i+1, N+1):
        if j<=X or i>=Y:
            path = j-i
        else:
            path = min(j-i, abs(X-i)+abs(j-Y)+1)
        cnt_dict[path] += 1

for i in range(1,N):
    print(cnt_dict[i])
