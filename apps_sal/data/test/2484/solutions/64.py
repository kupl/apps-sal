n = int(input())
a = list(map(int, input().split()))
ll = 0
rr = 0
llrr = 0
result = 0
for ll in range(n):
    while rr < n and a[rr] & llrr == 0:
        llrr += a[rr]
        rr += 1
    result += rr - ll
    llrr = llrr ^ a[ll]
print(result)
