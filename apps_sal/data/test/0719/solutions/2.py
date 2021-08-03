ls = []
cnt = 0


def gen(num, rem):
    if len(num) > 8:
        return
    if rem == 0:
        ls.append(int(num))
    for i in range(rem + 1):
        gen(num + str(i), rem - i)


for i in range(1, 10):
    gen(str(i), 10 - i)

ls.sort()
n = int(input())
print(ls[n - 1])
