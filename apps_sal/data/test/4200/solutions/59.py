N, M = list(map(int, input().split()))
num_list = list(map(int, input().split()))

X = sum(num_list)

s = 0
while s < N:
    if num_list[s] < (X / (4 * M)):
        del num_list[s]
        N = N - 1
    else:
        s = s + 1

if len(num_list) >= M:
    print('Yes')
else:
    print('No')
