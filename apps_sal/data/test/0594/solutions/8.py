n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

max_a = max(max(a), 2 * min(a))

wrong_pass = True
for c in b:
    if c <= max_a:
        wrong_pass = False
        break

if wrong_pass:
    print("%d" % max_a)
else:
    print("-1")
