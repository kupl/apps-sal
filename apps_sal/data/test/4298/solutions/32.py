N,D = map(int,input().split())

for i in range(20):
    if 2*D*i + i >= N:
        print(i)
        return
