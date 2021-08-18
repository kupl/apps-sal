N = int(input())
txn = []
for i in range(N):
    txn.append([int(i) for i in input().split()])

ima = [0, 0, 0]
for i in range(N):
    dist = abs(ima[1] - txn[i][1]) + abs(ima[2] - txn[i][2])

    if dist > (txn[i][0] - ima[0]):
        print("No")
        return

    if dist % 2 != (txn[i][0] - ima[0]) % 2:
        print("No")
        return

    ima = txn[i]

print("Yes")
