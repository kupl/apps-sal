n = int(input())
c = list(map(int, input().split()))

l, r = 0, n - 1
while c[l] == c[-1]:
    l += 1
while c[r] == c[0]:
    r -= 1

print(max(r, n - 1 - l))
