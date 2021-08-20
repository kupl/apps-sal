N = input()
N = N.translate(str.maketrans({'1': '9', '9': '1'}))
print(int(N))
