n = int(input())
l = list(map(int, input().split()))
m = {}
m2 = set()
for i in range(1, 10**6 + 1):
    m[i] = 0
for i in range(n):
    m[l[i]] += 1
    m2.add(l[i])
    if l[i] >= 2:
        m2.add(l[i] - 1)
m1 = []

for i in range(10**6, 1, -1):
    if m[i] % 2 == 1 and m[i - 1] > 0:
        m[i] -= 1
        m[i - 1] += 1
    elif m[i] % 2 == 1:
        m[i] -= 1
for i in m2:
    if m[i] != 0:
        m1.append(i)
m1.sort(reverse = True)

cnt = 0
for i in range(len(m1)):
    cnt += (m[m1[i]]//4)*(m1[i]**2)
    if m[m1[i]] % 4 == 2 and i != len(m1) - 1:
        m[m1[i + 1]] -= 2
        cnt += m1[i + 1]*m1[i]
print(cnt)
        
        
    
        

