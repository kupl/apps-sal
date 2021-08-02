import statistics
N = int(input())
A = list(map(int, input().split()))
ans = []
for a in A:
    ans.append(a)
    ans.append(a - 1)
    ans.append(a + 1)
mode = statistics.mode(ans)
print(ans.count(mode))
