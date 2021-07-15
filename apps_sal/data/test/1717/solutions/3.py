N = int(input())
factor = set([2, 3, 4, 5, 7, 9, 10, 11, 13, 17, 19, 23, 29])
res = 1
for i in range(2, N+1):
    if i in factor:
        res *= i
print((res+1))

