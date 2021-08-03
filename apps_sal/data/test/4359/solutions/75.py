l = [int(input()) for i in range(5)]
lm = l
lm = [(i + 9) // 10 * 10 for i in l]
lr = [10 - i % 10 if i % 10 != 0 else 0 for i in l]
print((sum(lm) - max(lr)))
