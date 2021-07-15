def generate(num, pref):
    nonlocal res
    if num == 0:
        res += 1
        if pref == n:
            print(res)
            return
    else:
        generate(num - 1, pref + '4')
        generate(num - 1, pref + '7')

n = input()
num = len(n)
res = 0
for i in range(1, num):
    res += 2 ** i
generate(num, '')
print(res)
