import math
n, a, b = map(int, input().split())
our_list = list(map(int, input().split()))
for i in range(n):
    print(our_list[i] - (math.ceil(((our_list[i] * a) // b) * b / a)), end = ' ')
