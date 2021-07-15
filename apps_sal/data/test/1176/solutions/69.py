n = int(input())
a = list(map(int, input().split()))

a.sort()
abs_a = [abs(x) for x in a]
minus = []

for x in a:
    if x < 0:
        minus.append(x)

tmp = sum(abs_a)

if len(minus) % 2 == 0:
    print(tmp)
else:
    print(tmp - min(abs_a)*2)
