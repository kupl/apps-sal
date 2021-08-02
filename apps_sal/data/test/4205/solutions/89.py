n = int(input())
l = list(map(int, input().split()))
l2 = sorted(l)
c = 0
for i in range(len(l)):
    if l[i] != l2[i]:
        c += 1
print("YES" if c <= 2 else "NO")
