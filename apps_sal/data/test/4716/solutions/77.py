N, K = map(int,input().split())
l = list(map(int,input().split()))

l.sort(reverse=True)
snake = []

for i in range(K):
    snake.append(l[i])

print(sum(snake))
