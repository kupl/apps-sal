n = int(input())
res = 1
t1 = 0
t2 = 0
for i in range(n):
    new_t1, new_t2 = list(map(int, input().split()))
    if t1 == t2:
        res += min(new_t1 - t1, new_t2 - t2)
    elif t1 > t2:
        if new_t1 > new_t2:
            res += max(0, new_t2 - t1 + 1)
        else:
            res += new_t1 - t1 + 1
    elif t2 > t1:
        if new_t2 > new_t1:
            res += max(0, new_t1 - t2 + 1)
        else:
            res += new_t2 - t2 + 1
    t1, t2 = new_t1, new_t2
print(res)
