n = int(input())
m = int(input())
flash = []
for i in range(n):
    flash.append(int(input()))
flash.sort(key=lambda x: -x)
prefix = 0
for i in range(n):
    prefix += flash[i]
    if m <= prefix:
        print(i + 1)
        break
else:
    print('?')
