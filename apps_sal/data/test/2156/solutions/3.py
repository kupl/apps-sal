N = int(input())

arr = input()
arr = [int(x) for x in arr.split(' ')]

prefix = [0] * N

s = 0
for i in range(N):
    s += arr[i]
    prefix[i] = s

# print(prefix)

Q = int(input())

for i in range(Q):
    arr = input()
    L, R = [int(x) for x in arr.split(' ')]
    if L == 1:
        range_sum = prefix[R - 1]
    else:
        range_sum = prefix[R - 1] - prefix[L - 2]

    # print(range_sum)

    print(range_sum // 10)
