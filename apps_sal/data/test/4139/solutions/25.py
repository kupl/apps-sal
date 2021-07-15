from itertools import product
n_str = input()
n = int(n_str)
l = len(n_str)
e_list = ["3", "5", "7"]
ans = 0
for i in range(3, l + 1):
    for temp in list(product(e_list, repeat=i)):
        if "3" in temp and "5" in temp and "7" in temp:
            num = int("".join(temp))
            if num <= n:
                ans += 1
print(ans)
