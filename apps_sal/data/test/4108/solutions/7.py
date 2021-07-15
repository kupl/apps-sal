from collections import Counter
s = list(input())
t = list(input())

s_count = Counter(s)
t_count = Counter(t)

# s,tそれぞれの各文字の出現回数が同じであれば一致させられる
if sorted(s_count.values()) == sorted(t_count.values()): print("Yes")
else: print("No")
