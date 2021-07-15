N = int(input())
num_list = [int(input()) for _ in range(N)]
num = 0
for i in range(N):
    if num_list[num] == 2:
        print(i+1)
        return
    num = num_list[num]-1
print(-1)
