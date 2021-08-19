n = int(input())
ans = 0


def check_even(n):
    n_l = list(str(n))
    n_count = len(n_l)
    if n_count % 2 == 0:
        return True
    else:
        return False


for i in range(1, n + 1):
    if check_even(i):
        continue
    ans += 1
print(ans)
