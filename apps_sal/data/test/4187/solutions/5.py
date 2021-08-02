n = int(input())
l = list(map(int, input().split())) * 2
cb = 0
cl = 0
for i in l:
    if i == 1:
        cl += 1
    else:
        cb = max(cb, cl)
        cl = 0
cb = max(cb, cl)
print(cb)
