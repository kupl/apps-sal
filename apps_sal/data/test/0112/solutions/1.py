def gen(cur, used, x):
    pos.add(cur)
    if x == n:
        return
    for j in range(n):
        if not used[j]:
            for i in a[j]:
                if i != 0 or x != 0:
                    used[j] = True
                    gen(cur * 10 + i, used, x + 1)
                    used[j] = False


n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
pos = set()
gen(0, [False] * n, 0)
x = 1
while x in pos:
    x += 1
print(x - 1)
