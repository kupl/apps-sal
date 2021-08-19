N = int(input())
A = list(map(int, input().split()))
cnt = 0
flag = True
while flag:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] //= 2
        else:
            flag = False
            break
    else:
        cnt += 1
        continue
    break
print(cnt)
