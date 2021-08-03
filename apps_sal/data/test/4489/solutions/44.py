n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
s_set = list(set(s))
win = max(s.count(s_set[i]) - t.count(s_set[i]) for i in range(len(s_set)))
print(max(0, win))
