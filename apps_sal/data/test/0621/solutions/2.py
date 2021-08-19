def readln():
    return tuple(map(int, input().split()))


(n,) = readln()
cnt = al = 0
ans = []
for a in readln():
    if cnt == 2 and a < 0:
        ans.append(al)
        cnt = al = 0
    al += 1
    cnt += a < 0
ans.append(al)
print(len(ans))
print(*ans)
