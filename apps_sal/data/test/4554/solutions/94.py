(W, a, b) = list(map(lambda x: int(x), input().split(' ')))
m = min([a, b])
M = max([a, b])
if M - m > W:
    print(M - m - W)
else:
    print(0)
