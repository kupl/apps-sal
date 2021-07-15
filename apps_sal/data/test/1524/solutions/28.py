S = input()
ans = [0 for _ in range(len(S))]
cnt = 0
for i, s in enumerate(S):
    if s == "R":
        cnt += 1
    else:
        x = cnt // 2
        ans[i] += x
        ans[i - 1] += x + cnt % 2
        cnt = 0
cnt = 0
for i, s in enumerate(S[::-1]):
    if s == "L":
        cnt += 1
    else:
        i += 1
        x = cnt // 2
        ans[-i] += x
        ans[-i + 1] += x + cnt % 2
        cnt = 0
print((*ans))

