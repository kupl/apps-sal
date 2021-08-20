n = int(input())
a = list(map(int, input().split()))
c = 0
for ia in a:
    if ia < 0:
        c += 1
a = list(map(abs, a))
if c % 2 == 0:
    print(sum(a))
else:
    print(sum(a) - 2 * min(a))
