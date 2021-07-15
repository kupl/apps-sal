n = input()
list01 = input().split()
list02 = [int(a) for a in list01]

print(max(list02) - min(list02))
