'''input
3
1 2 3
'''

from sys import stdin, stdout


# main starts
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
val1 = 0
for i in arr:
    val1 ^= i

store = [0] * (n + 1)
for i in range(1, n + 1):
    c = n // i
    store[0] += c
    store[i] -= c
    r = n % i
    if r >= 1:
        store[1] += 1
        if r + 1 <= n:
            store[r + 1] -= 1

store[0] %= 2
for i in range(1, len(store)):
    store[i] += store[i - 1]
    store[i] %= 2

for i in range(len(store)):
    if store[i] != 0:
        val1 ^= i
print(val1)
