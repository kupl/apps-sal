import bisect
a = int(input())
b = [1]
for i in range(2, 34):
    j = 2
    while i ** j <= 1000:
        b.append(i ** j)
        j += 1
c = sorted(b)
index = bisect.bisect_right(c, a)
print(c[index - 1])
