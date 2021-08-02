n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a_max = max(a)
a_second = sorted(a)[-2]
for i in range(n):
    print(a_max if a[i] != a_max else a_second)
