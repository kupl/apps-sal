ins = input()
ins = ins.split()
list(map(int, ins))
n, s, t = list(map(int, ins))
ins = input()
ins = ins.split()
ins = list(map(int, ins))
p = []
p.append(-1)
p += ins
ans = 0
while(s != t):
    ans += 1
    s = p[s]
    if(ans >= n):
        s = t
        ans = -1
print(ans)
