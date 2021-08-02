N, K = list(map(int, input().split()))
pt = list(map(int, input().split()))
T = input()

pc_hand = [0] * N
my_hand = [0] * N

for i in range(N):
    if T[i] == 'r':
        pc_hand[i] = 0
    elif T[i] == 's':
        pc_hand[i] = 1
    else:
        pc_hand[i] = 2

point = 0

for i in range(N):
    if i >= K and T[i] == T[i - K] and (my_hand[i - K] + 1) % 3 == pc_hand[i - K]:
        my_hand[i] = pc_hand[i]
    else:
        my_hand[i] = (pc_hand[i] - 1) % 3
        point += pt[my_hand[i]]

print(point)
