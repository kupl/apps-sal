n = int(input())
str_dict = dict()
for i in range(n):
    s = input()
    if s not in str_dict:
        str_dict[s] = 1
    else:
        str_dict[s] += 1

m = int(input())
for i in range(m):
    t = input()
    if t not in str_dict:
        str_dict[t] = -1
    else:
        str_dict[t] -= 1

res = max(0, sorted(list(str_dict.values()))[-1])
print(res)
