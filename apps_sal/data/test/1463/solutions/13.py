def int_input():
    return list(map(int, input().split()))


n = int(input())
matr = [list(int_input()) for i in range(n)]
good = True
for row in range(n):
    nums = set(matr[row])
    for col in range(n):
        num = matr[row][col]
        if num == 1:
            continue
        cur_good = False
        for i in range(n):
            cur_good |= num - matr[i][col] in nums
        good &= cur_good
print('Yes' if good else 'No')
