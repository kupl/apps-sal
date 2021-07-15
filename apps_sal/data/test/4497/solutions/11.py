n = int(input())
ans = 0
answer = 1
for i in range(1, n+1):
    cnt = 0
    num = i
    while num % 2 == 0:
        num //= 2
        cnt += 1
    if cnt > ans :
        answer = i
        ans = cnt 
print(answer)
