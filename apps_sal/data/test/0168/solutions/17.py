n = int(input())
ops = input()
curr = 0
ans = 0
for op in ops:
    curr += -1 if op == '-' else 1
    ans = max(ans, -curr)
for op in ops:
    ans += -1 if op == '-' else 1
print(ans)
