n = int(input())
ar = set(map(int, input().split()))

Max = max(ar)
ans = ()
flag = 0
for i in ar:
    j = 1
    while i + j <= Max:
        if i + j in ar:
            ans = (i, i + j)
            flag = 1
            if i + 2 * j in ar:
                print("3")
                print(i, i + j, i + 2 * j)
                return
        j *= 2
if flag == 1:
    print("2")
    print(*ans)
else:
    print("1")
    print(Max)
