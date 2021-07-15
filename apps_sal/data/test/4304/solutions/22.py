a,b = map(int,input().split())
c = 0
for i in range(1,b- a + 1):
    c += i
print(c - b)
