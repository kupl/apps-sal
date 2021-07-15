s = int(input())
k = []
for i in range(0,s):
    a=input()
    k.append(a)
amount = []
for i in range(s):
    amount.append(0)
    for j in range(s):
        if k[i] == k[j]:
            amount[i] += 1
ans = max(amount)
print (ans)
