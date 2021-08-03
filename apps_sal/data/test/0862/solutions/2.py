n = int(input())
ta = input().split()
a = [0]
for i in ta:
    a.append(int(i) + n)
mn = 1000000000000000000
mner = 1
for i in range(1, n + 1):
    if (a[i] - i) // n < mn:
        mn = (a[i] - i) // n
        mner = i
print(mner)
