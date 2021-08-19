radi = input()
list = radi.split(' ')
N = int(list[0])
days = input()
total = 0
a = days.split(' ')
for items in a:
    total += int(items)
if total > N:
    print(-1)
else:
    print(N - total)
