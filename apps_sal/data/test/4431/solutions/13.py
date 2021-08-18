n, k = list(map(int, input().strip().split()))
x = list(input())
a = input().strip().split()
xx = 0
op = 0
for i in x:
    if(i in a):
        xx += 1
    else:
        op = op + (xx * (xx + 1) // 2)
        xx = 0
op = op + (xx * (xx + 1) // 2)
print(op)
