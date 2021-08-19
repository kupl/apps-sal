([n, k], speed) = (list(map(int, input().split())), sorted(map(int, input().split()), reverse=True))
print(speed[k - 1])
