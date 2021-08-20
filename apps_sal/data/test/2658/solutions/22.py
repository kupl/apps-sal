(n, k) = [int(x) for x in input().split()]
a_list = [int(x) - 1 for x in input().split()]
ci = 0
while k:
    if k & 1:
        ci = a_list[ci]
    k >>= 1
    a_list = [a_list[a_list[i]] for i in range(n)]
print(ci + 1)
