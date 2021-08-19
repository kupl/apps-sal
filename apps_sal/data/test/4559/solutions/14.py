N = int(input())
a = list(map(int, input().split()))
sum_ = 1
if 0 in a:
    print(0)
else:
    for i in range(N):
        sum_ *= a[i]
        if sum_ > 10 ** 18:
            sum_ = -1
            break
    print(sum_)
