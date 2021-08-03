x = int(input())
ans_s = x // 11
ans_a = x % 11
if 1 <= ans_a <= 6:
    print(2 * ans_s + 1)
elif ans_a == 0:
    print(2 * ans_s)
else:
    print(2 * ans_s + 2)
