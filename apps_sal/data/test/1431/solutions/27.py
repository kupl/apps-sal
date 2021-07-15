n = int(input())
list_A = list(map(int, input().split()))
list_N = [0]*n

for i in range(n, 0, -1):
    k, cnt = 0, 0
    while True:
        if k+i > n:
            break
        if list_N[k+i-1] == 1:
            cnt += 1
        k += i
    list_N[i-1] = (list_A[i-1]+cnt) % 2

ans = []
for i in range(n):
    if list_N[i] == 1:
        ans.append(i+1)
print(len(ans))
print(*ans)
