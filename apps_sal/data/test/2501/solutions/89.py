n = int(input())
a = list(map(int, input().split()))
b1,b2,dic,ans = [],[],{},0
for i, j in enumerate(a):
    b1.append(j-i)
    b2.append(-j-i)
for i, j in zip(b1, b2):
    if i in dic:
        ans += dic[i]
    if j in dic:
        dic[j] += 1
    else:
        dic[j] = 1
print(ans)
