from collections import Counter 
n = int(input())
a = list(map(int, input().split()))
s = set(a)
c = Counter(a)
t = [0] * (10**6 + 1)
for i in s:
    for j in range(i, 10**6+1, i):
        t[j] += 1

ans = len([1 for i in s if t[i] == 1 and c[i] == 1])
print(ans)


