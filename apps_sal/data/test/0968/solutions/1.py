n = int(input())
l = [input().split() for i in range(n)]
p = [int(x) - 1 for x in input().split()]

cur = ""
poss = True
for i in range(n):
    per = l[p[i]]
    if per[0] > cur:
        if per[1] > cur:
            cur = min(per[0], per[1])
        else:
            cur = per[0]
    else:
        if per[1] > cur:
            cur = per[1]
        else:
            poss = False
            break
print("YES" if poss else "NO")
