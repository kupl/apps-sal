N = int(input())
W = [input() for _ in range(N)]
used = []

first = W[0]
used.append(first)

for index in range(1, len(W)):
    if W[index][0] == W[index-1][-1] and W[index] not in used:
        used.append(W[index])
    else:
        print("No")
        return
print("Yes")

