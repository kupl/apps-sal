s = input().rstrip()
k = int(input())
n = len(s)
ss = set()
for i in range(n):
    for j in range(1, k + 1):
        ss.add(s[i:i + j])
print(sorted(ss)[k - 1])
