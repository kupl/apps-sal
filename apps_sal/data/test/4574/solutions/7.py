n = int(input())
A = list(map(int, input().split()))
d = {0:4}
for a in A:
    d[a] = d.get(a, 0)+1
longest = 0
for i in d:
    if d[i]>=2:
        longest = max(longest, i)
d[longest]-=2

longest_2nd = 0
for i in d:
    if d[i]>=2:
        longest_2nd = max(longest_2nd, i)
print(longest*longest_2nd)
