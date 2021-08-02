import sys
n = int(input())
t = list(map(int, input().split()))
for i in range(1, len(t) - 1):
    if t[i] - t[i - 1] != t[i + 1] - t[i]:
        print(t[len(t) - 1])
        return
print(t[len(t) - 1] + (t[1] - t[0]))
