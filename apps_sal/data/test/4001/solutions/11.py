n = int(input())
a = list(map(int, input().split()))
a.sort()
num = max(a)
d = dict()
for i in range(n):
    d[a[i]] = 0
for i in range(n):
    d[a[i]] += 1
a = list(set(a))
v = []
for i in range(len(a)):
    if d[a[i]] == 2 or num % a[i] != 0:
        v.append(a[i])
num2 = max(v)
print(num, num2)
