N = int(input())
A = [int(input()) for _ in range(N)]
A = [a - 1 for a in A]
fin = set()
cnt = 0
i = 0
while True:
    if i in fin:
        cnt = -1
        break
    if i == 1:
        break
    cnt += 1
    fin.add(i)
    i = A[i]
print(cnt)
