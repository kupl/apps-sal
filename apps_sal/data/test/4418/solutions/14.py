n = int(input())
a = [int(x) for x in input().split()]
exist = [4,8,15,16,23,42]
s = set(exist)
waiting = [0] * 6
ans = 0
for x in a:
    if x not in s:
        ans += 1
        continue
    if x == 4:
        waiting[0] += 1
        continue
    pos = exist.index(x)
    if waiting[pos - 1] == 0:
        ans += 1
        continue
    waiting[pos - 1] -= 1
    if x != 42:
        waiting[pos] += 1
# print(waiting)
for i in range(6):
    ans += (i + 1) * waiting[i]
print(ans)
    

