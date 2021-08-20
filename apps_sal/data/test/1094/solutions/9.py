def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x in seen:
            continue
        seen.add(x)
        result.append(x)
    return result


a = int(input())
c = []
for i in range(a):
    c += [input()]
print(*unique(reversed(c)), sep='\n')
