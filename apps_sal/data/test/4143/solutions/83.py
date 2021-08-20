import math
N = int(input())
X = [int(input()), int(input()), int(input()), int(input()), int(input())]
print(math.ceil(N / min(X)) + 4)
