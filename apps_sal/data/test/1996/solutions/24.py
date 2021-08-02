n = int(input())
poss = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
strikes = 0
found = False
for i in range(n - 1):
    a = input().split()
    if a[0] == '!':
        poss = poss.intersection(set(a[1]))
        if found:
            strikes += 1
    elif a[0] == '.':
        poss = poss.difference(set(a[1]))
    else:
        poss = poss.difference(set(a[1]))
        if found:
            strikes += 1
    if len(poss) == 1:
        found = True
print(strikes)
