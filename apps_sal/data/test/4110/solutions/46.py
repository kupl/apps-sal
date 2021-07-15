d, g = map(int, input().split())
pc = [list(map(int,input().split())) for _ in range(d)]
ans = g//100 + 1

for i in range(2**d):
    count = 0
    total = 0
    for j in range(d):
        if (i >> j) & 1 == 1:
            count += pc[j][0]
            total += (j+1)*100*pc[j][0] + pc[j][1]

    if total >= g:
        ans = min(ans, count)
    else:
        for k in reversed(range(d)):
            if ((i >> k) & 1) == 0:
                for _ in range(pc[k][0]):
                    if total >= g:
                        ans = min(ans, count)
                        break
                    count += 1
                    total += (k+1)*100

print(ans)
