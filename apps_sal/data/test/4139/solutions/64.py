from itertools import product
n_str = input()
n = int(n_str)
ans = 0
for i in range(3, len(n_str) + 1):
    for temp in list(product(['3', '5', '7'], repeat=i)):
        if '3' in temp and '5' in temp and ('7' in temp) and (int(''.join(temp)) <= n):
            ans += 1
print(ans)
