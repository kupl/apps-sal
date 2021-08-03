
n = input()
years = tuple([int(x) for x in input().split(' ')])

print((max(years) + min(years)) // 2)
