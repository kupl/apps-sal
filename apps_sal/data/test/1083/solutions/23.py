

n = int(input())

res_list = []

desired_sum = (n * (n + 1) // 2)
s = 0

for j in range(n, 0, -1):
    if 2 * (s + j) <= desired_sum:
        s += j
        res_list += [j]

print(desired_sum - 2 * s)
print(str(len(res_list)), " ".join(map(str, res_list)))
