N = int(input())
K = int(input())
j = 1


def func(x, y):
    r = x * 2 if x * 2 < x + y else x + y
    return r


for i in range(N):
    j = func(j, K)
print(j)
