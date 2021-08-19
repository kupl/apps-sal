(n, m) = [int(_) for _ in input().split()]
ans = []
for i in range(n):
    ary = []
    inp = input().split()
    for q in inp:
        ary.append(int(q))
    ans.append(min(ary))
print(max(ans))
