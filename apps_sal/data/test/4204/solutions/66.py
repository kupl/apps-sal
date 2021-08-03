s = input()
k = int(input())
n = 5000 * 10**12

for i, c in enumerate(s):
    if c != '1':
        print(c)
        break
    if i + 1 == k:
        print((1))
        break
