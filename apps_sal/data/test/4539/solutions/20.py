a = input()
print('YNeos'[int(a) % sum([int(i) for i in a]) != 0::2])
