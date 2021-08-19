length = list(map(int, input().split()))
length.sort()
print(int(length[0] * length[1] / 2))
