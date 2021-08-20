N = int(input())
S = list((input() for x in range(N)))
M = int(input())
T = list((input() for y in range(M)))
count = []
for n in range(N):
    count.append(S.count(S[n]) - T.count(S[n]))
max_count = max(count)
if max_count < 0:
    print(0)
else:
    print(max_count)
