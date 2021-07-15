c, v0, v1, a, l = map(int, input().split())
cur = v0
rem = c
tmp = 0
res = 0
while rem > 0 :
    res += 1
    rem = rem - (cur - tmp)
    cur = min(cur + a, v1)
    tmp = l
print(res)
