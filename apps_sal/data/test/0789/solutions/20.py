j = int(input())
s = [7, 4]
s1 = s
for i in range(11):
    ns = [i * 10 + 4 for i in s1] + [i * 10 + 7 for i in s1]
    s += ns
    s1 = ns

print(sorted(s).index(j) + 1)
