n = int(input())
a = list(map(int, input().split()))
evens = list()
odds = list()

for x in a:
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)

ret = sum(evens)

odds.sort()

i = len(odds) - 1

while i - 1 >= 0:
    ret += odds[i] + odds[i - 1]
    i -= 2

print(ret)
