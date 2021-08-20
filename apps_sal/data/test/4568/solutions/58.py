N = int(input())
S = str(input())
_sum = 0
visited = set()
_sum_visited = set()
max_size = len(set(S))
for n in range(N - 1):
    if S[n] in S[n + 1:] and S[n] not in visited:
        _sum += 1
    elif S[n] in visited and S[n] not in S[n + 1:]:
        _sum -= 1
    visited.add(S[n])
    _sum_visited.add(_sum)
    last_size = len(set(S[n + 1]))
    ans = max(_sum_visited)
    if ans == max_size:
        break
print(max(_sum_visited))
