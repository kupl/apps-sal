n = int(input())
a = list(map(int,input().split()))
ans = 0
cnt_minus = 0
cnt_zero = 0
m = 10**9
for i in a:
    ans += abs(i)
    if i<0:
        cnt_minus += 1
    if i==0:
        cnt_zero +=1
    m = min(m,abs(i))

if cnt_minus % 2 == 0 or cnt_zero !=0:
    print(ans)
else:
    print((ans-2*m))

