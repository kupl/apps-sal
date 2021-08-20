from bisect import bisect_left
n = int(input())
hurui = [True for _ in range(100010)]
prime_lst = []
for i in range(2, 100010):
    if not hurui[i]:
        continue
    prime_lst.append(i)
    for j in range(i * i, 100010, i):
        hurui[j] = False
pos = bisect_left(prime_lst, n)
print(prime_lst[pos])
