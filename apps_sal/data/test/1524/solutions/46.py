S = input()
N = len(S)

ans = [0] * N

cnt = 0
for i, s in enumerate(S):
    if s == "R":
        cnt += 1
    else:
        ans[i] += cnt // 2
        ans[i - 1] += cnt - cnt // 2
        cnt = 0

ans.reverse()
cnt = 0
for i, s in enumerate(S[::-1]):
    if s == "L":
        cnt += 1
    else:
        ans[i] += cnt // 2
        ans[i - 1] += cnt - cnt // 2
        cnt = 0

ans.reverse()
print((*ans))
