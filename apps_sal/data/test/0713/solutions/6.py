n, m = list(map(int, input().split()))
s = min(m, n) + 1
print(s)
for i in range(s):
    print(i, s - i - 1)
