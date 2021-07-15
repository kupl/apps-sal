n = int(input())
a = list(map(int, input().split()))
inc = set([])
dec = set([])
for i in a:
    if i not in inc:
        inc.add(i)
    elif i not in dec:
        dec.add(i)
    else:
        print("NO")
        return
inc = list(inc)
dec = list(dec)
inc.sort(reverse = True)
dec.sort()
print("YES")
print(len(dec))
print(*dec)
print(len(inc))
print(*inc)
