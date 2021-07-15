a,b,k = map(int,input().split())

k = k-1
i = a
while True:
    print(i)
    i += 1
    if  i > a + k or i > b:
        break
if i < b-k:
    i = b-k
while i <= b:
    print(i)
    i += 1
