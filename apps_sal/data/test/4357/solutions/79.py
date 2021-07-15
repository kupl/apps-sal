list01 = list(map(int, input().split()))
list02 = sorted(list01, reverse=True)
a = list02[0] * 10 + list02[1] + list02[2]
print(a)
