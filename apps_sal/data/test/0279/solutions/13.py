__author__ = 'clumpytuna'
v1, v2 = map(int, input().split(" "))
t, d = map(int, input().split(" "))
sum = v1
z = d
for i in range(2, t):
    if ((v1+d) - (t-i)*d) <= v2:
        v1 += d
        sum += v1
        #print(v1)
    else:
        while ((v1+z) - (t-i)*d) > v2:
            z -= 1
        v1 = v1 + z
        sum += v1
        #//print(v1, 'df')
        z  = d
print(sum+v2)
