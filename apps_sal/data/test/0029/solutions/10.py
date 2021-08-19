digits = [int(x) for x in input()]
difference = sum(digits[0:3]) - sum(digits[3:])
helper = []
if difference < 0:
    helper = [9 - x for x in digits[:3]] + digits[3:]
else:
    helper = digits[:3] + [9 - x for x in digits[3:]]
helper = sorted(helper)[::-1]
n = 0
sum_ = 0
for x in helper:
    if sum_ >= abs(difference):
        break
    sum_ += x
    n += 1
print(n)
