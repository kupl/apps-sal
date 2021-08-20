s = sorted((x for x in input()))
t = sorted([x for x in input()], reverse=True)
print('Yes' if s < t else 'No')
