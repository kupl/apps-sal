n = int(input())
a = list(map(int, input().split()))
a = list(sorted(a, reverse=True))
new_a = [0] * n
left_pivot = n // 2
right_pivot = left_pivot + 1
if n % 2 == 0:
    left_pivot, right_pivot = left_pivot - 1, right_pivot - 1
for i in range(n):
    if i % 2 == 0:
        new_a[left_pivot] = a[i]
        left_pivot -= 1
    else:
        new_a[right_pivot] = a[i]
        right_pivot += 1
print(' '.join(map(str, new_a)))
