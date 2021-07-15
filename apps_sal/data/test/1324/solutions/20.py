kal = []
kal = [int(x) for x in input().split()]
s = input()
print(sum([kal[int(x) - 1] for x in s]))

