n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum_a = [0]
sum_b = [0]

counta = 0
for x in a:
    counta += x
    if counta <= k:
        sum_a.append(counta)
    else:
        break

countb = 0
for y in b:
    countb += y
    if countb <= k:
        sum_b.append(countb)
    else:
        break


n = len(sum_b)

ans = 0

for i in range(len(sum_a)):
    for j in reversed(range(n)):
        if sum_a[i] + sum_b[j]<= k:
            ans = max(ans,i+j)
            n = j+1
            break
    else:
        break


print(ans)
