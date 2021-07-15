n = int(input())
for i in range(n, 0, -1):
    if n % i != 0:
        continue
    bz = f'{i:b}'
    if bz.count('0') + 1 != bz.count('1'):
        continue
    elif set(bz[:len(bz)//2 + 1]) == {'1'}:
        print(i)
        break


