N = int(input())
dishes = list(map(int, input().split()))
satisfaction = list(map(int, input().split()))
additional = list(map(int, input().split()))

res = 0

for i in range(N-1):
    res += satisfaction[i]

    if dishes[i] + 1 == dishes[i+1]:
        res += additional[dishes[i] - 1]

print((res + satisfaction[-1]))



