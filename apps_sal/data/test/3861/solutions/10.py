import math

_ = input()

m = None
aa = list(map(int, input().split()))

print(max([a for a in aa if a < 0 or (int(math.sqrt(a)) * int(math.sqrt(a)) != a)]))
