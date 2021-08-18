N = int(input())
S = input()

not_r = 0
not_b = 0
for i, s in enumerate(S):
    if i % 2 == 0:
        if s != "r":
            not_r += 1
    else:
        if s != "b":
            not_b += 1
ans = max(not_r, not_b)

not_r = 0
not_b = 0
for i, s in enumerate(S):
    if i % 2 == 0:
        if s != "b":
            not_b += 1
    else:
        if s != "r":
            not_r += 1
ans = min(ans, max(not_r, not_b))
print(ans)
