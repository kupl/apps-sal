N = int(input())
N_List = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if i + 1 != N_List[i]:
        cnt += 1
print(('NO', 'YES')[cnt <= 2])
