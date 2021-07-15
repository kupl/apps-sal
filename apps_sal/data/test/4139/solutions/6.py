from itertools import product
n_str = input()
n = int(n_str)
ans = 0
for i in range(3, len(n_str) + 1):
    for temp in list(product(["3", "5", "7"], repeat=i)):
        temp_set = set(temp)
        if "3" in temp_set and "5" in temp_set and "7" in temp_set and int("".join(temp)) <= n:
            ans += 1
print(ans)
