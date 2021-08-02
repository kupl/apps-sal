alph = __import__('string').ascii_lowercase
for _ in range(int(input())):
    n = int(input())
    g = {i: 0for i in alph}
    for _ in range(n):
        for i in input():
            g[i] += 1
    print('YNEOS'[any(g[i] % n for i in g)::2])
