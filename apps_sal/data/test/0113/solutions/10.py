(n, k) = [int(x) for x in input().split()]
n1 = n
cnt5 = cnt2 = 0
for i in range(k):
    if n1 % 2 == 0:
        n1 //= 2
        cnt2 += 1
    else:
        break
for i in range(k):
    if n1 % 5 == 0:
        n1 //= 5
        cnt5 += 1
    else:
        break
if cnt2 >= k and cnt5 >= k:
    print(n)
else:
    print(n * 2 ** (k - cnt2) * 5 ** (k - cnt5))
