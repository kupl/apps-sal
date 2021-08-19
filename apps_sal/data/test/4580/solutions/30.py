import math
N = int(input())
A = [math.floor(a / 400) if a < 3200 else 3200 for a in list(map(int, input().split()))]
set_A = set([a for a in A if a != 3200])
print(*[max(1, len(set_A)), len(set_A) + A.count(3200)], sep=' ')
