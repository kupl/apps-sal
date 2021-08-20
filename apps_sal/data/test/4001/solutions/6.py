input()
d = list(map(int, input().split()))
a = max(d)
for i in range(2, a + 1):
    if a % i == 0:
        d.remove(i)
print(a, max(d))
