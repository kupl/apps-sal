a,b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    l,r = list(str(i))[:3], list(str(i))[2:][::-1]
    if l == r: cnt += 1
print(cnt)
