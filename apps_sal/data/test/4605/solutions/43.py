N,A,B = map(int,input().split())

ans = 0
for i in range(N):
    n = i + 1
    arr = list(map(int,str(n)))
    summ = sum(arr)
    if summ >= A and summ <= B:
        ans += n
print(ans)
