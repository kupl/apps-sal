import collections

mod = 10**9 + 7
n = int(input())
arr = list(map(int, input().split()))
cnt = collections.Counter(arr)
for key in cnt.keys():
    if cnt[key] == 2:
        K = key
pos1 = -1
pos2 = -1
for i in range(n + 1):
    if arr[i] == K:
        if pos1 == -1:
            pos1 = i
        else:
            pos2 = i
A = pos1
B = pos2 - pos1 - 1
C = n - pos2
facts = [1]
for i in range(1, n + 1):
    facts.append((facts[-1] * i) % mod)
revfacts = [1]
for i in range(1, n + 1):
    revfacts.append(pow(facts[i], mod - 2, mod))
ans = []
for i in range(1, n + 2):
    ways1 = 0
    if i <= A + B + C:
        ways1 = (facts[A + B + C] * revfacts[i] * revfacts[A + B + C - i]) % mod
    ways2 = 0
    if i >= 2 and i - 2 <= A + B + C:
        ways2 = (facts[A + B + C] * revfacts[i - 2] * revfacts[A + B + C - (i - 2)]) % mod
    ways3 = 0
    if i >= 1 and i - 1 <= A + C:
        ways3 = (facts[A + C] * revfacts[i - 1] * revfacts[A + C - (i - 1)]) % mod
    ways4 = 0
    if i >= 1 and i - 1 <= A + B + C:
        ways4 = (2 * facts[A + B + C] * revfacts[i - 1] * revfacts[A + B + C - (i - 1)] - 2 * ways3) % mod
    ans.append((ways1 + ways2 + ways3 + ways4) % mod)
for val in ans:
    print(val)
