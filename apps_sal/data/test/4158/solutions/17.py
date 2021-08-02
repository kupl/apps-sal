n = int(input())
a = set(map(int, input().split()))
ans = []
f = 0
for i in a:
    c = 1
    for p in range(31):
        if(i + c in a):
            ans = [i, i + c]
            if(i + c * 2 in a):
                print(3)
                print(i, i + c, i + c * 2)
                f = 1
                break
        c *= 2
    if(f):
        break
if(f == 0):
    if(ans):
        print(2)
        print(*ans)
    else:
        print(1)
        print(min(a))
