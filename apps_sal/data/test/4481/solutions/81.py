import collections
n = int(input())
s = [input() for _ in range(n)]
c = collections.Counter(s)
sorted_c = c.most_common()
max = sorted_c[0][1]
dict_c = []
for i in range(len(sorted_c)):
    if sorted_c[i][1] == max:
        dict_c.append(sorted_c[i][0])
    else:
        break
dict_c.sort()
for i in range(len(dict_c)):
    print(dict_c[i])
