n = int(input())
a = list(map(int, input().split()))
di = {0: 0}
k = 1
q = 1
for i in a:
    if i in di:
        del di[i]
    else:
        q += 1
    di[k] = i
    k += 1
print(q)
