m, n = map(int, input().split())
p = list(map(int, input().split()))
a=0

while True:
    if m-a not in p:
        print(m-a)
        break
    elif m+a not in p:
        print(m+a)
        break
    a+=1
