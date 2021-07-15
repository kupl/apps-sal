N = int(input())
A = list(map(int, input().split()))

cnt = len([i for i in A if i < 0])
PA = list(map(abs, A))

if cnt % 2 == 0:
    print(sum(PA))
else:
    print(sum(PA) - min(PA) * 2)
