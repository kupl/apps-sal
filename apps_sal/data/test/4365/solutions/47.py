K = int(input())

even = K // 2
odd = K - even
if K == 3:
    print(2)
else:
    print(even * odd)
