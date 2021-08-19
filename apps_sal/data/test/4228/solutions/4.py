(n, l) = map(int, input().split())
apple = []
for i in range(1, n + 1):
    apple.append(l + i - 1)
eat = sorted(apple, key=lambda x: abs(x))
print(sum(apple) - eat[0])
