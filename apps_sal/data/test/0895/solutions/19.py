n = int(input())
l = [int(i) for i in input().split()]
l.sort()
t = int(input())
st = 0
maxi = 0
for end in range(n):
    while l[end] - l[st] > t:
        st += 1
    if end - st + 1 > maxi:
        maxi = end - st + 1
        ans = (st, end)
print(maxi)
# print(ans)
