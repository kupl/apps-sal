def Evkl(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


n = int(input())
string = input()
x = []
lens = []
for i in string.split(" "):
    x.append(int(i))
x.sort()
for i in range(0, n - 1):
    lens.append(abs(x[i] - x[i + 1]))
lens.sort()
min_len = lens[0]
max_len = lens[-1]
for i in range(1, n - 1):
    if min_len == 1:
        break
    if lens[i] % min_len != 0:
        min_len = Evkl(lens[i], min_len)
print(abs(x[0] - x[-1]) // min_len - n + 1)
