# alpha = "abcdefghijklmnopqrstuvwxyz"
prime = 998244353
# INF = 1000_000_000

# from heapq import heappush, heappop
# from collections import defaultdict
# from math import sqrt
# from collections import deque
# from math import gcd

n = int(input())
# arr = (map(int, input().split()))
arr = list(input().split())
count = [0 for i in range(11)]
count2 = [0 for i in range(11)]
for i in arr:
    count[len(i)] += 1
for i in range(1, 11):
    count2[i] = count2[i - 1] + count[i]
ans = 0
for i in arr:
    place = 1
    k = 1
    for j in range(len(i) - 1, -1, -1):
        # tmp = ans
        ans = (ans + (count2[10] - count2[k - 1]) * place * int(i[j])) % prime
        ans = (ans + (count2[10] - count2[k - 1]) * place * int(i[j]) * 10) % prime
        for l in range(1, k):
            ans = (ans + 2 * count[l] * pow(10, l + k - 1) * int(i[j])) % prime
        place = place * 100
        # print("check", int(i[j]), ans, ans-tmp)
        k += 1
print(ans)
