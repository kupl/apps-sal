l, r, k = [int(x) for x in input().split()]

x = 1

correct = False
while x <= r:
    if x >= l:
        print(x, end=" ")
        correct = True
    x *= k

if not correct:
    print("-1")
else:
    print("")

