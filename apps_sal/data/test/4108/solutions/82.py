from collections import Counter
s = input()
t = input()

s_count = Counter(s)
t_count = Counter(t)
if sorted(s_count.values()) == sorted(t_count.values()):
    print("Yes")
else:
    print("No")
