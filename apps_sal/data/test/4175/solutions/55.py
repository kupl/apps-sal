N = int(input())
W = [input() for n in range(N)]
for i in range(N - 1):
    if W[i][-1] != W[i + 1][0] or W[i + 1] in W[0:i:1]:
        print('No')
        break
else:
    print('Yes')
