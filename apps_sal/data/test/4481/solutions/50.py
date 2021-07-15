n = int(input())

dct = {}

for i in range(n):
    s = input()
    if s in dct:
        dct[s] += 1
    else:
        dct[s] = 1

max_num = max(dct.values())
ans = []
sorted_dct = sorted(dct.items())
 
for x in sorted_dct:
    if x[1] >= max_num:
        ans.append(x[0])
 
print(*ans, sep='\n')
