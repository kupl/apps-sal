n, k = map(int, input().split())
s = list(map(int, input().split()))
s = sorted(s)
m = 0
if len(s)%k!= 0:
    m = 2*(max(s[:len(s)%k]) - 1)
    s = s[len(s)%k:]
while s != []:
    l = len(s)
    m += (s[l-1] - 1)*2
    s = s[:l-k]
print(m)
