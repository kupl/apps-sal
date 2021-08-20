n = int(input())
ans = 1
current_zero_count = 0
for i in range(1, n + 1):
    target_zero_count = list(map(int, bin(i)[2:])).count(0)
    if n == 1:
        break
    elif target_zero_count > current_zero_count:
        current_zero_count = target_zero_count
        ans = i
print(ans)
