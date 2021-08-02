n = int(input())
s = list(map(int, input().split()))
x = n
d = 2
c = 0
used = [False] * n
while x > 0:
    c = x
    for i in range(n):
        if used[i] == True:
            continue
        if s[i] % d != 0:
            x -= 1
            used[i] = True
    d *= 2
print(d // 4, c)
