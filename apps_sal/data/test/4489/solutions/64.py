N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]

st_dict = {}

for i in range(N):
    if s[i] not in st_dict.keys():
        st_dict[s[i]] = 1
    else:
        st_dict[s[i]] += 1
for i in range(M):
    if t[i] not in st_dict.keys():
        st_dict[t[i]] = -1
    else:
        st_dict[t[i]] -= 1

if max(st_dict.values()) < 0:
    print(0)
else:
    print(max(st_dict.values()))
