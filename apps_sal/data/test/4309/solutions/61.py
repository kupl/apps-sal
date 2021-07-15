n = int(input())
for i in range(1, 10):
    l = [i, i, i]
    num = int(''.join(map(str, l)))
    if n <= num:
        print(num)
        break
