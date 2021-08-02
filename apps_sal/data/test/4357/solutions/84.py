li_1 = a, b, c = list(map(int, input().split()))
li = sorted(li_1, reverse=True)
print(int(str(li[0]) + str(li[1])) + li[2])
