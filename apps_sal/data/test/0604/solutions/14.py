n = int(input())
a = set(list(map(int, input().split())))
ans = len(a)
if 0 in a:
    ans -= 1
print(ans)
