b1 , q , l , m = list(map(int, input().split()))
s = set(map(int , input().split()))
ans = 0
cnt = 0
while abs(b1) <= l:
    if b1 not in s:
        ans += 1
    cnt += 1
    if cnt == 100000:
        break
    b1 *= q
    
if ans >= 50000:
    print('inf')
else:
    print(ans)

