n, m = map(int, input().split())
arr = list(map(int, input().split()))
prep = list(map(int, input().split()))
x = [0] * m
# print(x)
#mp = dict()
total = sum(prep) + m
c = 0
# for i in range(1,m+1):
#	mp[i] = prep[i-1]
# print(mp)
st = set()

ans = 0
flag = 0
for i in range(n):
    st.add(arr[i])
    # print(st,i+1,total)
    if(arr[i] and prep[(arr[i] - 1)] <= i and not x[(arr[i] - 1)]):
        x[(arr[i] - 1)] = 1
        c += 1
    if ((0 in st and len(st) == (m + 1)) or (0 not in st and len(st) == m)) and (i + 1) >= total and arr[i]:
        ans = i + 1
        flag = 1
        break
# print(c)
if flag and c == m:
    print(ans)
else:
    print(-1)
