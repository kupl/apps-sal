N = int(input())
A = [int(i) for i in input().split()]

start = -1
max_l = 0
A.append(0)

for i in range(N + 1):
    if(A[i] == 0):
        l = i - start - 1
        # print(l)
        if(l > max_l):
            max_l = l
        start = i

print(max_l)
