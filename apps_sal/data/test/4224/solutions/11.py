input()
print((sum([len(bin(int(a)&-int(a)))-3 for a in input().split()])))

