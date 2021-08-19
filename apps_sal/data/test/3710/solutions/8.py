# https://codeforces.com/problemset/problem/687/B
MAX = 1000000
n, k = map(int, input().split())
ancient = [int(x) for x in input().split()]

isPrime = [0 for x in range(MAX + 1)]
count = [0 for x in range(MAX + 1)]

for x in range(2, MAX + 1):
    if not isPrime[x]:
        for y in range(x, MAX + 1, x):
            isPrime[y] = x

for val in ancient:
    while val > 1:
        p = isPrime[val]
        c = 0
        while val % p == 0:
            c += 1
            val = val // p
        count[p] = max(count[p], c)

flag = True
while k > 1:
    flag &= (count[isPrime[k]] > 0)
    count[isPrime[k]] -= 1
    k = k // isPrime[k]
print("Yes" if flag else "No")
