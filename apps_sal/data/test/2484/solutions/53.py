n = int(input())
a_list = [int(x) for x in input().split()]

ans = 0
temp_xor = a_list[0]
temp_sum = a_list[0]
r = 0
for l in range(n):
    while r < n:
        if temp_xor != temp_sum:
            break
        r += 1
        if r < n:
            temp_xor ^= a_list[r]
            temp_sum += a_list[r]
    ans += r - l
    temp_xor ^= a_list[l]
    temp_sum -= a_list[l]
print(ans)
