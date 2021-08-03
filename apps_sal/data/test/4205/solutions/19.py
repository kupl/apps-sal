input()
a = [*map(int, input().split())]
print('YNEOS'[sum(i != j for i, j in zip(a, sorted(a))) > 2::2])
