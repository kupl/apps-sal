n = int(input())
li = list(map(int,input().split()))
li1 = []

for i in li:
    li1.append(1/i)

su = sum(li1)
print((1/su))

