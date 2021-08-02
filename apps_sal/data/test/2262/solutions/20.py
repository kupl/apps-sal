n = input()
roots = set(tuple(sorted(set(w))) for w in input().split())
print(len(roots))
