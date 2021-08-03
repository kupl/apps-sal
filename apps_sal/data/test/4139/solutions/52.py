from itertools import product

n = int(input())
ans = 0
for i in range(len(str(n)) - 2):
    for j in list(product("753", repeat=i + 3)):
        if int(''.join(j)) <= n and len(set(j)) == 3:
            ans += 1
print(ans)
