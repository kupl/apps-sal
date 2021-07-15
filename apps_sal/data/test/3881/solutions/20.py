
3

ans = set()

def gen(cur, n, ops):
    if len(cur) == n:
        ans.add(cur)
    else:
        for t in ops[ord(cur[0]) - ord("a")]:
            gen(t + cur[1:], n, ops)


n, q = list(map(int, input().split()))
ops = [[] for i in range(6)]
for i in range(q):
    s, t = input().split()
    ops[ord(t[0]) - ord('a')].append(s)

gen("a", n, ops)
print(len(ans))

