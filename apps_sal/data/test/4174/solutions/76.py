(N, X) = list(map(int, input().split()))
ls1 = list(map(int, input().split()))
x = 0
ii = 1
for i in ls1:
    x = x + i
    if x > X:
        break
    ii += 1
print(ii)
