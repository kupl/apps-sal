N = int(input())
S = [input() for _ in range(N)]
dict_s = dict()
for s in S:
    if s in dict_s:
        dict_s[s] += 1
    else:
        dict_s[s] = 1

sorted_s = sorted(dict_s.items(), key=lambda x: x[1], reverse=True)
max_s = []
max_count = -1
for s in sorted_s:
    if s[1] >= max_count:
        max_s.append(s[0])
        max_count = s[1]

for s in sorted(max_s):
    print(s)
