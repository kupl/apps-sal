S = list(input())

ans = []

for s in S:
    if s == "B":
        if len(ans) > 0:
            del ans[-1]
    else:
        ans.append(s)

print("".join(ans))
