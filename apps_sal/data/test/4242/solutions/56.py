A, B, K = map(int, input().split())
cnt = 0
for i in range(max(A, B)):
    num = max(A, B) - i
    if A % num == 0 and B % num == 0:
        cnt += 1
    if cnt == K:
        break
print(num)
