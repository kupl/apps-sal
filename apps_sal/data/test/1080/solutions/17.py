n = int(input())
l = list(map(int, input().rstrip().split()))

s = sum(l)
ma = max(l)
if (s % 2 == 0) and (ma <= s / 2):
    print("YES")
else:
    print("NO")
