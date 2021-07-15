import math
for i in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))
    print(math.ceil(sum(t)/n))
