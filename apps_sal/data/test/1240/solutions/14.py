n = int(input())
l = []
r = []
suml  = 0
sumr  = 0
for i in range(n):
    a, b = input().split(' ')
    l.append(int(a))
    r.append(int(b))
    suml += int(a)
    sumr += int(b)
diff = abs(suml-sumr)
index = -1
for i in range(n):
    if abs((suml-l[i]+r[i])-(sumr-r[i]+l[i])) > diff:
        diff = abs((suml-l[i]+r[i])-(sumr-r[i]+l[i]))
        index = i
print(index+1)
