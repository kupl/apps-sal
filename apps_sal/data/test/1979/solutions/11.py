from collections import Counter
n = int(input())
t = [0] * n
for i, v in  enumerate(map(int, input().split())):
    t[v-1] = i
for i, v in  enumerate(map(int, input().split())):
    t[v-1] -= i
    t[v-1] %= n
print(max(Counter(t).values()))

