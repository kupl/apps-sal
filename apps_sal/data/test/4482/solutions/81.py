n = int(input())
a_list = [int(x) for x in input().split()]

a_sum = sum(a_list)
f = a_sum // n
c = (a_sum + n - 1) // n
b = f if abs(a_sum - f * n) < abs(a_sum - c * n) else c

ans = 0
for a in a_list:
    ans += (a - b) ** 2
print(ans)
