n = int(input())
(mn, mx) = ([], [])
for i in range(n):
    b = list(map(int, input().split()))
    if b[0] > b[1]:
        mx.append(b + [i + 1])
    else:
        mn.append(b + [i + 1])
if len(mx) > len(mn):
    ans = sorted(mx)
else:
    ans = sorted(mn, reverse=True)
print(len(ans))
print(*[x[2] for x in ans])
