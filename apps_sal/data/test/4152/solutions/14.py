n = int(input())
a = list(map(int, input().split()))
b = [2 ** i for i in range(33)]
d = dict()
ans = 0
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in a:
    flag = False
    for j in b:
        if j - i > 0:
            if i != j - i:
                if j - i in d.keys():
                    flag = True
            elif j - i in d.keys() and d[j - i] > 1:
                flag = True
    if flag == False:
        ans += 1

print(ans)
