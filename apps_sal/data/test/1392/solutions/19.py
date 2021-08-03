def all_zero(mas):
    for i in mas:
        if i != 0:
            return False
    return True


I = [int(i) for i in input().split()]
n, k = I[0], I[1]
ans = 0
for i in range(n):
    pretender = input()
    k_mas = [1] * (k + 1)
    for digit in pretender:
        if int(digit) <= k:
            k_mas[int(digit)] = 0
    if all_zero(k_mas):
        ans += 1
print(ans)
