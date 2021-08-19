N = int(input())
arr = sorted(list(map(int, input().split())))
(fidx, ridx) = (0, N - 1)
flag = True
for _ in range(N - 1):
    if flag:
        ridx -= 1
        flag = False
    else:
        fidx += 1
        flag = True
print(arr[fidx])
