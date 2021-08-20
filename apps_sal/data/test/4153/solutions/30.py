S = input()
N = len(S)
cnt = 0
for s in S:
    if s == '0':
        cnt += 1
print(2 * min(cnt, N - cnt))
