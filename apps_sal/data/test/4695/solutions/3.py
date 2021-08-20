(a, b, c) = ([1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], [2])
print('YNeos'[len(set([0 if i in a else [1, 2][i in b] for i in list(map(int, input().split()))])) != 1::2])
