S = list(input())
k = S.pop(0)
ii = 0
for i in S:
    if k == i:
        pass
    else:
        ii += 1
        k = i
print(ii)
