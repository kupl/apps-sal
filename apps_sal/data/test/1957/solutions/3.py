n, a, b = [int(x) for x in input().split()]
o = []
s = 0
for x in input().split():
    s += int(x)
    o.append(int(x))

s1 = o[0]
o[0] = 0
o.sort()
count = 0
while(s1*a < b*s):
    s -= o.pop()
    count+=1
print(count)

