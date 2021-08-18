s = input()
t = input()

s_map = [[] for i in range(26)]
t_map = [[] for i in range(26)]
n = len(s)

for i in range(n):
    si = ord(s[i]) - ord("a")
    ti = ord(t[i]) - ord("a")

    s_map[si].append(i)
    t_map[ti].append(i)

s_map = sorted(s_map)
t_map = sorted(t_map)

if s_map == t_map:
    print("Yes")
else:
    print("No")
