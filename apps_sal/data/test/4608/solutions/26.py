N = int(input())
A = [0]*(N+1)
for i in range(1,N+1):
    A[i] = int(input())

is_visited_list = [0]*(N+1)

loop = False
now_visit = 1
cnt = 0
while True:
    if is_visited_list[now_visit] == 1:
        loop = True
        break
    else:
        is_visited_list[now_visit] = 1
    
    now_visit = A[now_visit]
    if now_visit == 2:
        cnt +=1
        break
    else:
        cnt +=1

if loop:
    print(-1)
else:
    print(cnt)
