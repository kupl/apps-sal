n = input()

def f(x):
    return sum(list(map(int, list(n))))

if int(n) % f(n) == 0:
    print('Yes')
else:
    print('No')
