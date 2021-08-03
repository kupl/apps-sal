n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))
dict = {}
for v in arr:
    if v in dict:
        dict[v] += 1
    else:
        dict[v] = 1

if x:
    res = 0
    for v in list(dict.keys()):
        if (v ^ x) in dict and (v ^ x) > v:
            res += dict[v] * dict[v ^ x]
    print(res)
else:
    print(sum([x * (x - 1) // 2 for x in list(dict.values())]))
