n = int(input())
a = [int(x) for x in input().split()]
ans = max(a) ^ a[-1]
print(ans)

