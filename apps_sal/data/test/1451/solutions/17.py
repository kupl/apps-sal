n, k = map(int, input().split())
print(len([i for i in input().split() if i.count('4') + i.count('7') <= k]))
