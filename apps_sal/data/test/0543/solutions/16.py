n = int(input())
ps = [int(x) for x in input().split(' ')]

f = True

for i in range(n):
    if ps[i] % 2 == 1:
        if i == n - 1 or ps[i + 1] == 0:
            f = False
            break
        else:
            ps[i + 1] -= 1

print("YES" if f else "NO")
