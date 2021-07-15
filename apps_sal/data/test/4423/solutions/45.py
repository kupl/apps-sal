N = int(input())
SP = []
for i in range(N):
    S, P = input().split()
    SP.append([i+1, S, int(P)])

sort_SP = sorted(SP, key = lambda x: (x[1], -x[2]))

for ans in sort_SP:
    print((ans[0]))


