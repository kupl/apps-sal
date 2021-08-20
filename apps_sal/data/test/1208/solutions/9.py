n = int(input())
l = [0] * (10 ** 6 + 1)
capacity = 0
cur = 0
for i in range(n):
    s = input().split()
    visitor = int(s[1])
    if s[0] == '+':
        l[visitor] = 1
        cur += 1
        if cur > capacity:
            capacity = cur
    elif l[visitor] == 0:
        capacity += 1
    else:
        l[visitor] = 0
        cur -= 1
print(capacity)
