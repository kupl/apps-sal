n = int(input())
def R(): return map(int, input().split())


l = list(R())
l.sort()
s, m = 0, 1000000007
for i in range(n):
    s = (s + l[i] * (pow(2, i, m) - pow(2, n - 1 - i, m))) % m
print(s)
