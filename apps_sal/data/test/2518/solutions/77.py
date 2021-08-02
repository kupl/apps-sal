import math


def enough(HP, A, B, X):
    q = 0
    for i in range(len(HP)):
        q += max(math.ceil((HP[i] - B * X) / (A - B)), 0)
    if q <= X:
        return True
    else:
        return False


over = 10 ** 9
under = 0
HP = []
N, A, B = list(map(int, input().rstrip().split(" ")))
for i in range(N):
    HP.append(int(input()))

while abs(over - under) > 1:
    mid = (over + under) // 2
    if enough(HP, A, B, mid):
        over = mid
    else:
        under = mid
print(over)
