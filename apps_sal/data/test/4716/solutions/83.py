n, k = map(int, input().split())
l = list(map(int, input().split()))

l_sorted = sorted(l, reverse = True)
snake = 0
for i in range(k):
    snake += l_sorted[i]
print(snake)
