N = int(input())
S = input()
turns = (N - 11) // 2
cnt = 0
for i in range(N - 10):
    if S[i] == '8':
        cnt += 1
if cnt >= turns + 1:
    print('YES')
else:
    print('NO')
