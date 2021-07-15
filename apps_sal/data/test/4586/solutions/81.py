n = input().rstrip()
print(['No', 'Yes'][int(len(set(n[:3])) == 1 or len(set(n[1:])) == 1)])
