n,m = list(map(int, input().split()))
a = [int(x) for x in input().split()]
s = [0]
for x in a:
    s.append(s[-1] + x)
suc = 0
for i in range(m):
    l,r = list(map(int, input().split()))
    l -= 1
    kolko = s[r] - s[l]
    suc += max(0, kolko)
print(suc)

