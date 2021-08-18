import math

number = input().split(" ")
N = int(number[0])
T = int(number[1])
X = int(number[2])

time = math.ceil(N / T)

print(time * X)
