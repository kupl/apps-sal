n = int(input())
s = input()

l1 = "br" * (n // 2) + "b" * (n % 2)
l2 = "rb" * (n // 2) + "r" * (n % 2)

b1 = [0] * ((n // 2) +  (n % 2))
b2 = [0] * (n // 2) 
r1 = [0] * (n // 2) 
r2 = [0] * ((n // 2) +  (n % 2))

counter1 = 0
counter2 = 0

m1 = 0
m2 = 0
k1 = 0
k2 = 0

for i in range(n):
    if l1[i] == s[i]:
        if i % 2 == 0:
            b1[m1] = 1
            m1 += 1
        else:
            r1[k1] = 1
            k1 += 1            
    if l2[i] == s[i]:
        if i % 2 == 0:
            r2[m2] = 1
            m2 += 1
        else:
            b2[k2] = 1
            k2 += 1  


a1 = b1.count(0)
a2 = r1.count(0)

counter1 = abs(a2 - a1) + min(a1,a2)

a1 = b2.count(0)
a2 = r2.count(0)

counter2 = abs(a2 - a1) + min(a1,a2)

print(min(counter1, counter2))




