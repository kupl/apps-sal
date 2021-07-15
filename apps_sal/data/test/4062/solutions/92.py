def cin():
    return list(map(int, input().split()))

num = cin()
a = num[0]
b = num[1]
c = num[2]
d = num[3]

temp = []
temp.append(a * c)
temp.append(a * d)
temp.append(b * c)
temp.append(b * d)
print((max(temp)))

