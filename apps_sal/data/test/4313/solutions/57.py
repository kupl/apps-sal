n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
li = []
su = 0
for i in range(n):
    li.append(v[i]-c[i])

for i in li:
    if i > 0:
        su += i

print(su)
