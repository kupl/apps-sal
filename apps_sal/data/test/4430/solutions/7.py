n, m, k = [int(x)for x in input().split()]
ns = [int(x)for x in input().split()]
ns.reverse()
rem = k
num = 0
ans = []
for i in range(n):
    if rem >= ns[i]:
        rem -= ns[i]
        num += 1
    else:
        ans.append(num)
        rem = k - ns[i]
        num = 1
if num > 0:
    ans.append(num)

# print(ans)

if len(ans) <= m:
    print(sum(ans))
else:
    a = [sum(ans[:m])]
    # for i in range(m,len(ans)):
    #     a.append(a[-1]+ans[i]-ans[i-m])
    print(max(a))
