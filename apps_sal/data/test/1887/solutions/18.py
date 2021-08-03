n = int(input())
s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
c1 = 0
c2 = 0
for i in range(n):
    temp1 = max(c1, c2 + s1[i])
    temp2 = max(c2, c1 + s2[i])
    c1 = temp1
    c2 = temp2
print(max(c1, c2))
