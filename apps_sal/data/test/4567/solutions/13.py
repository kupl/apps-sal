N = int(input())
s = sorted([int(input()) for i in range(N)])
ans = sum(s)
if ans % 10 == 0:
    for i in s:
        if i % 10 == 0:
            pass
        else:
            ans -= i
            if ans % 10 != 0:
                break
if ans % 10 == 0 and ans == sum(s):
    print(0)
else:
    print(ans)
