n = int(input())
s = [int(input()) for _ in range(n)]

ans = sum(s)
if ans % 10 != 0:
    print(ans)
else:
    if all([i % 10 == 0 for i in s]):
        print(0)
    else:
        print(ans - min([i for i in s if i % 10 != 0]))
