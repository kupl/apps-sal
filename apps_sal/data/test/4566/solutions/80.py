N, M = map(int,input().split())
ab_list = []

for i in range(M):
    a, b = map(int,input().split())
    ab_list.append(a)
    ab_list.append(b)
    
for i in range(1, N + 1):
    print(ab_list.count(i))
