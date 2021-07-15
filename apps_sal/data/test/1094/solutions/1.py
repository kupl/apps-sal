n = int(input())
a = set()
res = []
names_arr = []
for i in range(n):
    name = input()
    names_arr.append(name)
for i in range(1, len(names_arr) + 1):
    cur_name = names_arr[-i]
    if cur_name not in a:
        a.add(cur_name)
        res.append(cur_name)
for i in range(len(res)):
    print(res[i])
