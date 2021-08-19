n = int(input())
left = []
right = []
for i in range(n):
    (l, r) = input().split()
    left.append(int(l))
    right.append(int(r))
left = sorted(left)
right = sorted(right)
res = n
for i in range(n):
    res += max(left[i], right[i])
print(res)
