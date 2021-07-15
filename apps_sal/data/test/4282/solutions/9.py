n = int(input())

v = {}

for i in range(1, n + 1):
    v[i] = set(map(int, input().split()))

ans = []

ans_s = set()

ans.append(1)

ans_s.add(1)

while len(ans) < n:
    for i in v[ans[-1]]:
        if len(v[i].intersection(v[ans[-1]])) > 0 and i not in ans_s:
            ans.append(i)
            ans_s.add(i)
            break


print(" ".join(map(str, ans)))
