input()
print((sum([len(bin(a & -a)) - 3 for a in map(int, input().split())])))
