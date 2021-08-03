n, m = map(int, input().split())
l = [[] for _ in range(n)]
ans = ""
for i in range(m):
    s, c = map(int, input().split())
    l[s - 1].append(c)
if len(l) > 1 and 0 in l[0]:
    print(-1)
elif n == 1 and m == 0:
    print(0)
else:
    for j in l:
        if len(set(j)) > 1:
            print(-1)
            break
        elif len(j) == 0:
            if ans == "":
                ans += "1"
            else:
                ans += "0"
        else:
            ans += str(j[0])
    else:
        print(ans)
