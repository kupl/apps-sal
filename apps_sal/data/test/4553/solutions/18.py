(a, b) = map(int, input().split())
s = list(input())
ans = 'No'
if s.count('-') == 1:
    ind = s.index('-')
    alen = ind
    blen = len(s) - (ind + 1)
    if alen == a and blen == b:
        ans = 'Yes'
print(ans)
