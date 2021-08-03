n = int(input())
non_10 = [0]
a = []
for i in range(n):
    a.append(int(input()))
    if a[i] % 10 != 0:
        non_10.append(a[i])
s = sum(a)
non_10.sort()
if s % 10 == 0:
    if len(non_10) > 1:
        s -= non_10[1]
    else:
        s = 0
print(s)
