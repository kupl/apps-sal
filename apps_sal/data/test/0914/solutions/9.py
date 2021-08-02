s = input()
n = int(input())
cnt = {}
for c in s:
    if cnt.get(c) == None:
        cnt[c] = 1
    else:
        cnt[c] += 1

if (n < len(cnt)):
    print(-1)
else:
    ansNum = 0;
    while(True):
        ansNum += 1
        l = 0;
        char = []
        for c, v in cnt.items():
            need = (v + ansNum - 1) // ansNum
            l += need
            char.append((c, need))
        if (l > n):
            continue
        print(ansNum)
        ans = "".join([str(c[0]) * c[1] for c in char])
        ans = ans + 'a' * (n - len(ans))
        print(ans)
        break
