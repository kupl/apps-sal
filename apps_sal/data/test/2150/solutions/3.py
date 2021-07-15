n = int(input())
b = list(map(int, input().split()))
a = []
max_so_far = 0
for i in range(n):
    a.append(b[i]+max_so_far)
    max_so_far = max(max_so_far, a[-1])
print(*a)
