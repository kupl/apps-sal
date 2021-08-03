n = int(input())
a = list(map(int, input().split()))
b = 0
for i in a:
    if i < 0:
        b += 1
c = list(map(abs, a))
if b & 1 and n + 1 & 1:
    print(sum(c) - 2 * min(c))
else:
    print(sum(c))
