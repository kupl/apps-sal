from collections import defaultdict
(n, k) = map(int, input().split())
l = [int(i) for i in input().split()]
maxi = 0
left = -1
right = -1
ans = 0
d = defaultdict(int)
st = 0
end = 0
for end in range(n):
    d[l[end]] += 1
    if d[l[end]] == 1:
        ans += 1
    while ans > k:
        d[l[st]] -= 1
        if d[l[st]] == 0:
            ans -= 1
        st += 1
    if end - st + 1 > maxi:
        maxi = end - st + 1
        left = st
        right = end
print(left + 1, right + 1)
