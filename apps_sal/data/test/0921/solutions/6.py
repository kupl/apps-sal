n,w = map(int,input().split())
ai = list(map(int,input().split()))
ai2 = list(range(n))
ai3 = [0] * n
summ = 0
odd_num = 0
for num in ai:
    summ += num - num % 2
    odd_num += num % 2
for i in range(n):
    for j in range(i+1,n):
        if ai[j] > ai[i]:
            temp = ai[i]
            ai[i] = ai[j]
            ai[j] = temp
            temp = ai2[i]
            ai2[i] = ai2[j]
            ai2[j] = temp
w -= summ // 2 + odd_num
if w < 0:
    print(-1)
else:
    for i in range(n):
        temp = min(w,ai[i]//2)
        w -= temp
        ai3[ai2[i]] = ai[i]//2 + ai[i] % 2 + temp
    for num in ai3:
        print(num,end=" ")

