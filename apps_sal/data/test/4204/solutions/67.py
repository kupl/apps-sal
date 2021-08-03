s = input()
k = int(input())
d = 5 * 10**15
for i in s:
    if i == '1':
        k -= 1
    else:
        print(i)
        return
    if k <= 0:
        print(1)
        return
