m = input().split()
n = int(m[0])
j = int(m[1])
l1 = input().split()
l2 = input().split()
p = int(l1[j - 1]) + int(l2[0])
c = j
for i in range(j - 1):
    if p >= int(l1[i]) + int(l2[-1]):
        c -= 1
        l2.pop()
print(c)
