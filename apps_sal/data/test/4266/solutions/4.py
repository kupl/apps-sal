(K, X) = map(int, input().split())
black_stone = []
for i in range(X - K + 1, X + K):
    black_stone.append(i)
black_stone = [str(a) for a in black_stone]
black_stone = ' '.join(black_stone)
print(black_stone)
