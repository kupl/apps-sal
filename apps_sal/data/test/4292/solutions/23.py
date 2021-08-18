N, K = map(int, input().split())
fruit = input().split()
fruit = [int(x) for x in fruit]
fruit.sort()
print(sum(fruit[:K]))
