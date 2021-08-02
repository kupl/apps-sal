S = input()

zero_count = S.count("0")
one_count = S.count("1")

ans = 2 * min(int(zero_count), int(one_count))
print(ans)
