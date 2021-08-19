n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
cnt = 0
while a:
    f = a.pop()
    rm = []
    for x in a:
        if x % f == 0:
            rm.append(x)
    for x in rm:
        a.remove(x)
    cnt += 1
print(cnt)
