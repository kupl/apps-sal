n = int(input())
home = []
visit = []
for i in range(0, n):
    (h, v) = [int(string) for string in input().split()]
    home.append(h)
    visit.append(v)
res = 0
for hh in home:
    res += visit.count(hh)
print(res)
