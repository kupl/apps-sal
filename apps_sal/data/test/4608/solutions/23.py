n = int(input())
done = [False for _ in range(n)]
A = [int(input()) - 1 for _ in range(n)]
tmp = 0
for i in range(n + 1):
    if A[tmp] == 1:
        print((i + 1))

        break
    if done[tmp]:
        print((-1))
        break
    else:
        done[tmp] = True
    tmp = A[tmp]
else:
    print((-1))

