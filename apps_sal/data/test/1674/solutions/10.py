n, k =list(map(int, input().split()))
a = list(map(int, input().split()))
st = input()
pr = None
cl = 0
ans = 0
vs = []
for i, s in enumerate(st):
    if s == pr:
        cl +=1
        vs.append(a[i])
        pr=s
    elif pr is not None:
        vs.sort(reverse=True)
        ans += sum(vs[:k])

        pr = s
        cl = 1
        vs = [a[i],]
    else:
        pr = s
        cl +=1
        vs.append(a[i])
vs.sort(reverse=True)
ans += sum(vs[:k])
print(ans)


