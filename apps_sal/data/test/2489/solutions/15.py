n = int(input())
a = sorted(map(int, input().split()))
s = [0] * (m := (a[-1] + 1))
for x in a:
    s[x] += 1
for x in a:
    for j in range(x * 2, m, x):
        s[j] = 0
print(s.count(1))
