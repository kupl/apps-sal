n = int(input())
t, a = list(map(int, input().split()))
h = list(map(int, input().split()))
a1 = []
a2 = []
for i in range(n):
    tt = abs((t - h[i]*0.006) - a)
    a1.append(tt)
    a2.append(i+1)
ans = {}
ans.update(list(zip(a1, a2)))
small = sorted(a1, reverse=False)[0]
print((ans[small]))

