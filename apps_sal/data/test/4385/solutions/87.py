a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
K = int(input())

LIST = [a, b, c, d, e]
LIST = sorted(LIST)
if LIST[-1] - LIST[0] <= K:
    print('Yay!')
else:
    print(':(')
