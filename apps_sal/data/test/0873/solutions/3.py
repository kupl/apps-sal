import sys

def get_d(d1, d2):
    if d1 > d2:
        d1, d2 = d2, d1
    return min(d2 - d1, 10 - d2 + d1)

#fin = open("input.txt", 'r')
fin = sys.stdin

n = int(fin.readline())
s1 = fin.readline().strip()
s2 = fin.readline().strip()
ans = 0
for i in range(n):
    ans += get_d(int(s1[i]), int(s2[i]))
print(ans)
