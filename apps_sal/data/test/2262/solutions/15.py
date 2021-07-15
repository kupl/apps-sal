n = int(input())
lns = input().split()
ans = set()
for ln in lns:
    ans.add(''.join(sorted(set(ln))))
print(len(ans))
