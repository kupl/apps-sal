r = input()
n = input()
length = len(n)
g = n.count("1")
same = False
nums = 0
if len(r) < length:
    print(0)
else:
    if (r[:len(n)].count("1") - g) % 2 == 0:
        same = True
        nums += 1
    for i in range(len(r) - len(n)):
        if r[i] != r[i + len(n)]:
            same = not same
        if same:
            nums += 1
print(nums)
