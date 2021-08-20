input()
print(len(set((tuple(sorted(list(set(x)))) for x in input().split()))))
