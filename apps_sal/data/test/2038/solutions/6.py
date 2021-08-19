n = int(input())
l = list(map(int, input().split()))
ll = [-1] * (n + 1)
for i in range(n):
    ll[l[i]] = i
res = []
# print(ll)
for k in range(1, n + 1):
    i = k
    j = ll[k]
    # print(i,j+1)
    if(2 * abs((j + 1) - i) >= n):
        res.append((i, j + 1))
        l[i - 1], l[j] = l[j], l[i - 1]
        ll[l[i - 1]], ll[l[j]] = ll[l[j]], ll[l[i - 1]]
    elif(i != (j + 1)):
        if(2 * abs(j + 1 - n) >= n and 2 * abs(i - n) >= n):
            res.append((i, n))
            l[i - 1], l[n - 1] = l[n - 1], l[i - 1]
            ll[l[i - 1]], ll[l[n - 1]] = ll[l[n - 1]], ll[l[i - 1]]
            res.append((j + 1, n))
            l[j], l[n - 1] = l[n - 1], l[j]
            ll[l[j]], ll[l[n - 1]] = ll[l[n - 1]], ll[l[j]]
            res.append((i, n))
            l[i - 1], l[n - 1] = l[n - 1], l[i - 1]
            ll[l[i - 1]], ll[l[n - 1]] = ll[l[n - 1]], ll[l[i - 1]]
        elif(2 * abs(j + 1 - 1) >= n and 2 * abs(i - 1) >= n):
            res.append((i, 1))
            l[i - 1], l[1 - 1] = l[1 - 1], l[i - 1]
            ll[l[i - 1]], ll[l[1 - 1]] = ll[l[1 - 1]], ll[l[i - 1]]
            res.append((j + 1, 1))
            l[j], l[1 - 1] = l[1 - 1], l[j]
            ll[l[j]], ll[l[1 - 1]] = ll[l[1 - 1]], ll[l[j]]
            res.append((i, 1))
            l[i - 1], l[1 - 1] = l[1 - 1], l[i - 1]
            ll[l[i - 1]], ll[l[1 - 1]] = ll[l[1 - 1]], ll[l[i - 1]]
        else:
            # print("lol")
            if(i > (j + 1)):
                i, j = j + 1, i - 1
            res.append((i, n))
            l[i - 1], l[n - 1] = l[n - 1], l[i - 1]
            ll[l[i - 1]], ll[l[n - 1]] = ll[l[n - 1]], ll[l[i - 1]]
            res.append((j + 1, 1))
            l[j], l[1 - 1] = l[1 - 1], l[j]
            ll[l[j]], ll[l[1 - 1]] = ll[l[1 - 1]], ll[l[j]]
            res.append((n, 1))
            l[n - 1], l[1 - 1] = l[1 - 1], l[n - 1]
            ll[l[n - 1]], ll[l[1 - 1]] = ll[l[1 - 1]], ll[l[n - 1]]
            res.append((i, n))
            l[i - 1], l[n - 1] = l[n - 1], l[i - 1]
            ll[l[i - 1]], ll[l[n - 1]] = ll[l[n - 1]], ll[l[i - 1]]
            res.append((j + 1, 1))
            l[j], l[1 - 1] = l[1 - 1], l[j]
            ll[l[j]], ll[l[1 - 1]] = ll[l[1 - 1]], ll[l[j]]
    # if(l3==l):
        # break
    # print(l,ll,sep="\n")
print(len(res))
for i in res:
    print(i[0], i[1])
# print(l)
