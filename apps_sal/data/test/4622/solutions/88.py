n = int(input())
print('YNEOS'[len(set(map(int, input().split()))) != n::2])
