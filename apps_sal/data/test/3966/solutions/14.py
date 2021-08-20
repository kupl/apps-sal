n = int(input())
s = input()
x = list()
x = s.split()
y = sorted(x, key=int)
ans = 0
for i in range(n):
    ans += int(y[i]) * (i + 2)
ans -= int(y[n - 1])
print(ans)
