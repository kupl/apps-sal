S = list(map(int, list(input())))
N = len(S)
cnt = [0, 0]
for i in S:
    cnt[i] += 1
print(2 * min(cnt))
