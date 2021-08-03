from collections import Counter
n = int(input())
a = list(map(int, input().split()))
ac = Counter(a)
count = 0
temp = 0
for i in ac:
    if ac[i] >= 3:
        if ac[i] % 2 == 0:
            count += (ac[i] - 2)
            ac[i] = 2
        else:
            count += (ac[i] - 1)
            ac[i] = 1

for j in ac:
    if ac[j] == 2:
        temp += 1
if temp % 2 == 0:
    count += temp
else:
    count += ((temp + 1))
print((n - count))
