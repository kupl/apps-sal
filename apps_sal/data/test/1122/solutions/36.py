N,M= list(map(int, input().split()))

num = list(range(1,N+1))
ans = []


if M % 2 == 0:
    for i in range(M // 2):
        ans.append([i+1,M+1-i])
    for i in range(M // 2):
        ans.append([i+2+M,2*M+1-i])


if M % 2 != 0:
    for i in range(M // 2):
        ans.append([i+1,M-i])
    for i in range(M - M//2):
        ans.append([i+1+M,2*M+1-i])


for an in ans:
    print((an[0],an[1]))

