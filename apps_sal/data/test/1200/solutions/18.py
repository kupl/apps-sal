def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
a = input()
a = int(a)
x = sorted(list(map(int, input().split())))
mn = 0
cnt = 0
i = 0
for i in range(a):
     if cnt > 0:
          mn = gcd(x[i] - x[i - 1], mn)
     cnt = cnt + 1
ans = 0
cnt = 0;
i = 0
for i in range(a):
     if cnt > 0:
          ans = ans + ((x[i] - x[i - 1]) // mn - 1)
     cnt = cnt + 1
print(ans)
