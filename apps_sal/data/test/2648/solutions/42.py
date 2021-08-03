N = int(input())
A = set()
cnt = 0


def count(n, Set):
    if not n in Set:
        Set.add(n)
        return 0
    else:
        return 1


for x in input().split():
    cnt += count(x, A)
if not cnt & 1:
    ans = N - cnt
else:
    ans = N - cnt - 1
print(ans)
