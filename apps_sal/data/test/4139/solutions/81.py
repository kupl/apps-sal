from itertools import product
n = int(input())
m = len(str(n))
ans = 0
for i in range(3,m+1):
    l = list(product('753',repeat=i))
    for _ in l:
        x = ''.join(list(_))
        if '7' in x and '5' in x and '3' in x:
            if n >= int(x):
                ans += 1
print(ans)
