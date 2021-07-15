########### E
H, W, M = map(int, input().split())
bombs = []
for _ in range(M):
    bomb = tuple(map(lambda x:int(x)-1, input().split()))
    bombs.append(bomb)

H_list = [0]*H
W_list = [0]*W
for h,w in bombs:
    H_list[h] += 1
    W_list[w] += 1
    
maxX = max(H_list)
maxY = max(W_list)

max_H = [i for i,k in enumerate(H_list) if k == maxX]
max_W = [i for i,k in enumerate(W_list) if k == maxY]

bombs = set(bombs)
for i in max_H:
    for k in max_W:
        if (i,k) not in bombs:
            print(maxX + maxY)
            return

print(maxX + maxY -1)
