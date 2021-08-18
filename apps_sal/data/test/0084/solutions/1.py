
def solve(x, a):
    if x < a:
        ans = 2 * x - a + 1
        ans //= 2
    else:
        ans = (a - 1) // 2
    return max(0, ans)


n = input()
optimal_nines = len(n)
if int(n[0]) < 5:
    optimal_nines -= 1
n = int(n)
if n <= 4:
    print((n * (n - 1)) // 2)
    quit()
ans = 0
for i in range(0, 9):
    curr_num = str(i) + '9' * optimal_nines
    curr_num = int(curr_num)
    ans += solve(n, curr_num)

print(ans)
