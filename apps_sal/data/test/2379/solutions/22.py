N, K, C = map(int, input().split())
S = input()
w = []
for i in range(len(S)):
    if S[i] == "o":
        w.append(i)
# print(w)
# early date
early = []
tmpwd = -1
for i in range(len(w)):
    if len(early) >= K:
        continue
    if tmpwd < 0:
        tmpwd = w[i]
    elif w[i] > tmpwd + C:
        tmpwd = w[i]
    else:
        continue
    early.append(w[i])
# print(early)

# later date
late = []
tmpwd = -1
for i in reversed(range(len(w))):
    if len(late) >= K:
        continue
    if tmpwd < 0:
        tmpwd = w[i]
    elif w[i] < tmpwd - C:
        tmpwd = w[i]
    else:
        continue
    late.append(w[i])

wd = set(early) & set(late)
early.sort()
late.sort()
# print(early,late)
for i in range(K):
    if early[i] == late[i]:
        print(early[i] + 1)
