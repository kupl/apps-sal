N = int(input())
X = list(map(int, input().split()))
D = [(x - round(sum(X) / N)) ** 2 for x in X]
print(sum(D))
