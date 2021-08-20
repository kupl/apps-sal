n = int(input())
p = []
for i in range(n):
    p.append(int(input()))
p.sort()
ans = sum(p)
if ans % 10 == 0:
    for i in p:
        if i % 10 != 0:
            ans -= i
            break
    if ans % 10 == 0:
        print(0)
    else:
        print(ans)
else:
    print(ans)
