x = int(input())
a = [int(x) for x in input().split()]
s = 0
mx = 0
for x in a:
    if x > mx:
        mx = x
    s += x
k = mx
while (True):
    s1 = 0
    for x in a:
        s1 += k - x
    if s1 > s:
        print(k)
        return
    k += 1
