n = int(input())
s1 = 2
s = [1]
a = list(map(int, input().split()))
for i in range(2, n):
    if a[i] != a[i - 1] + a[i - 2]:
        s.append(s1)
        s1 = 2
    else:
        s1 += 1
s.append(s1)
if n == 1:
    print(1)
else:
    print(min(max(s), n))
