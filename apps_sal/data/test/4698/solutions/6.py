n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = [list(map(int,input().split())) for i in range(m)]
ans = []
for num in p:
    print(sum(t) - t[num[0]-1] + num[1])
