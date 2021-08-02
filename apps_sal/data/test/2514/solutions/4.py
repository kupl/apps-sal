N = int(input())
As = list(map(int, input().split()))
Q = int(input())

count_array = [0] * (10**5 + 1)
for i in range(N):
    count_array[As[i]] += 1

sum = 0
for i in range(len(As)):
    sum += As[i]

for i in range(Q):
    x, y = list(map(int, input().split()))
    sum += count_array[x] * (y - x)
    print(sum)
    count_array[y] += count_array[x]
    count_array[x] = 0
