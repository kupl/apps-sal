n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
jud = 1
q = a[0]
ans = 0
for i in range(1, n):
    if(q == a[i]):
        jud += 1
    else:
        if(jud % 2 == 1):
            ans += 1
        jud = 1
        q = a[i]
if (jud % 2 == 1):
    ans += 1
if(n == 1):
    ans = 1
print(ans)
