from collections import defaultdict
n = int(input())
s = input()
count = defaultdict(int)
for c in s:
    count[c] += 1
max_count = max(count.values())
k = sum([1 for value in list(count.values()) if value == max_count])
mod = 10 ** 9 + 7
answer = 1
for i in range(n):
    answer = answer * k % mod
print(answer)
