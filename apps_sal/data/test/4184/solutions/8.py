n = int(input())
w = list(map(int, input().split()))

s = sum(w) / 2
count = 0
for i in w:
    count += i
    if count > s:
        countine = count - i
        break

if (count - s) - (s - countine) > 0:
    print((int(2 * (s - countine))))
else:
    print((int(2 * (count - s))))
