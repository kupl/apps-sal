r = input().split()
N = int(r[0])
L = int(r[1])
ans = 0
ans_li = []
for i in range(N):
    ans += L + (i + 1) - 1
    ans_li.append(L + (i + 1) - 1)
if 0 in ans_li:
    print(ans)
elif max(ans_li) > 0:
    print(ans - min(ans_li))
else:
    print(ans - max(ans_li))
