n = int(input())
h = list(map(int, input().split()))
mnx = -1
mxx = 10**8
avg = sum(h) // len(h)
avgx = avg + 1
s1 = 0
s2 = 0
for i in h:
    s1 += ((i - avg)**2)
    s2 += ((i - avgx)**2)
print(min(s1, s2))
