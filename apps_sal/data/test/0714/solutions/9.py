n = int(input())
l = list(map(int, input().split()))

lst = []
for i in range(n):
    lst.append([i, l[i]])

p_cnt = n // 2

one = sum(l) // p_cnt

while lst:
    f = lst[-1]
    for i in range(len(lst)):
        x = lst[i]
        if x[1] + f[1] == one:
            s = x
            print(f[0] + 1, s[0] + 1)
            lst.pop(i)
            lst.pop()
            break
