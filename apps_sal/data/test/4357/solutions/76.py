lst = list(map(int, input().split()))
lst.sort()
lst.reverse()
maximum = int(str(lst[0]) + str(lst[1])) + lst[2]
print(maximum)
