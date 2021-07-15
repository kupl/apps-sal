N = int(input())
A = [int(x) for x in input().split()]

pair = []
unpair = set()
for a in A:
    if a in unpair:
        pair.append(a)
        unpair.remove(a)
    else:
        unpair.add(a)

pair.sort()
pair.reverse()
if len(pair) <= 1:
    ans = 0
else:
    ans = pair[0] * pair[1]
print(ans)
