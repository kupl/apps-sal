S = input()
K = 10 ** 100
RL_counts = []
ptr = []
ans = [0] * len(S)
cnt = 1
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        cnt += 1
    else:
        RL_counts.append(cnt)
        if (S[i] == "L"):
            ptr.append(i - 1)
        cnt = 1
RL_counts.append(cnt)

for i in range(0, len(RL_counts), 2):
    ans[ptr[int(i / 2)]] += int((RL_counts[i] + 1) / 2) + int(RL_counts[i + 1] / 2)
    ans[ptr[int(i / 2)] + 1] += int(RL_counts[i] / 2) + int((RL_counts[i + 1] + 1) / 2)

print((" ".join(map(str, ans))))
