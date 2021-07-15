n = int(input())
a = [int(x) for x in input().split()]
ans = sum(a)
ans_li = []
q = int(input())

d = {}
for i in range(len(a)):
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1

for i in range(q):
    B,C = list(map(int,input().split()))
    if B not in d:
        ans_li.append(ans)
    else:
        num = d[B]
        dis = abs(B - C)
        if B >= C:
            ans_li.append(ans - (num * dis))
            ans = ans_li[-1]
        else:
            ans_li.append(ans + (num * dis))
            ans = ans_li[-1]

        if C not in d:
            d[C] = num
            d[B] = 0
        else:
            d[C] += num
            d[B] = 0

for aa in ans_li:
    print(aa)

