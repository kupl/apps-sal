n, k = map(int, input().split())
d = list(map(int, input().split()))

while True:
    for i in str(n):
        if int(i) in d:
            n += 1
            break
    
    else:
        print(n)
        break
