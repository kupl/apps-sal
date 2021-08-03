N, K = list(map(int, input().split()))
V = list(map(int, input().split()))

R = min(N, K)
point = 0
max_point = 0
hand = []

for i in range(R + 1):
    for a in range(i + 1):
        if i == a:
            hand = V[:a]
        else:
            hand = V[:a] + V[-(i - a):]
        negahand = [k for k in hand if k < 0]
        negahand.sort()
        if K - i > len(negahand):
            trash = -sum(negahand)
        else:
            trash = -sum(negahand[:K - i])
        point = sum(hand) + trash
        max_point = max(max_point, point)

print(max_point)
