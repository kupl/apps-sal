(k, x) = map(int, input().split())
number = []
for i in range(x - (k - 1), x + (k - 1) + 1):
    number.append(i)
number_str = [str(n) for n in number]
num = ' '.join(number_str)
print(num)
