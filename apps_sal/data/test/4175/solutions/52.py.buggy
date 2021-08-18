N = int(input())
W = [input() for i in range(N)]

if len(set(W)) != len(W):
    print("No")
    return

for i in range(N - 1):
    if W[i][-1] == W[i + 1][0]:
        continue
    else:
        print("No")
        return

print("Yes")
