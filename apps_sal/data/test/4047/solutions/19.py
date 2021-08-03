n = int(input())
a = list(map(int, input().split()))
s = 0
s1 = 0
for i in range(n):
    if a[i] % 2 == 0:
        s += 1
    else:
        s1 += 1
print(min(s, s1))
