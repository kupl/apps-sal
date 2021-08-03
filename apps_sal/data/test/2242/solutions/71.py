s = input()

len_s = len(s)

current = 0
mod_dict = dict()
mod_dict[0] = 1
for i in range(len_s - 1, -1, -1):
    c = s[i]
    current = (current + pow(10, len_s - i - 1, 2019) * int(c)) % 2019
    if current in mod_dict:
        mod_dict[current] += 1
    else:
        mod_dict[current] = 1

count = 0
for key in mod_dict:
    count += (mod_dict[key] * (mod_dict[key] - 1)) // 2

print(count)
