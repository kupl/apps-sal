n = int(input())
state = [int(e == '1') for e in input()]
l = [[*map(int, input().split())] for _ in range(n)]
res = sum(state)
for t in range(1, 1000):
    for i in range(n):
        if t >= l[i][1] and (t - l[i][1]) % l[i][0] == 0:
            state[i] ^= 1
    res = max(res, sum(state))
print(res)
