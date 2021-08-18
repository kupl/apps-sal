n = int(input())
A = list(map(int, input().split()))

abs_min = 10**9
flag = False
if A.count(0) >= 1:
    flag = True
neg_count = 0
ans = 0
for a in A:
    ans += abs(a)
    if a < 0:
        neg_count += 1
    if abs(a) < abs_min:
        abs_min = abs(a)
if neg_count % 2 == 0:
    flag = True

if flag:
    print(ans)
else:
    print(ans - 2 * abs_min)
