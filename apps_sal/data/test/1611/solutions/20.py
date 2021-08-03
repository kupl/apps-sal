n = int(input())
d = input().split()
d = [int(x) for x in d]
m = max(d)
d.remove(m)
S = 0
for i in d:
    S += i
print(m - S + 1)
