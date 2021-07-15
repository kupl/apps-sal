n = int(input())
a = list(map(str, input().split()))
b = []
'''
b = [str(a[0])]
if (n == 1):
    print(a[0])
    return

a = a[1:]

for i in a:
    b.append(str(i))
    b.reverse()
'''
'''
loop = int(n / 2)
loop_rest = n - loop

for i in range(loop):
    tar_index = (n - 1) - 2 * i
    tar = a[tar_index]

    b.append(str(tar))


if (n % 2 == 0):
    tar_index = 0
else:
    tar_index = 1

for i in range(loop_rest):
    b.append(str(a[tar_index]))
    tar_index += 2
'''

# 一つおきでListを取る場合。
# a[0::2]
# 1つ目：起点。
# 2つ目：Step

# a[::-1]
# > -1step,つまりReverse

if n % 2 == 1:
    print((" ".join((a[0::2][::-1] + a[1::2]))))
else:
    print((" ".join((a[1::2][::-1] + a[0::2]))))

