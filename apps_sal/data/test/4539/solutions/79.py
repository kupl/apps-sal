a = input()
print('YNeos'[int(a) % sum(map(int, a)) != 0::2])
