n = int(input())
a = list(map(int, input().split()))
left = 0
ans = 0
xor_sum = 0
normal_sum = 0
for (right, b) in enumerate(a):
    xor_sum ^= b
    normal_sum += b
    while xor_sum < normal_sum:
        xor_sum ^= a[left]
        normal_sum -= a[left]
        left += 1
    ans += right - left + 1
print(ans)
