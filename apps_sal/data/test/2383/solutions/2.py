n = int(input())
a = list(map(int, input().split()))
res = 0
num = 1
if 1 not in a:
    print(-1)
else:
    for ai in a:
        if ai == num: num += 1
        else: res += 1
    print(res)
