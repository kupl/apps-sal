N, K = map(int, input().split())
fruit = input().split()
#print(fruit)
fruit = [int(x) for x in fruit]
#print(fruit)
fruit.sort()
#print(fruit)
print(sum(fruit[:K]))
