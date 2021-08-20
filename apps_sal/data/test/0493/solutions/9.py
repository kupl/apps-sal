n = int(input())
a = input()


def work(a, b):
    l = [-1] * n
    for i in range(0, n):
        if a[i] == '.':
            l[i] = l[i - 1]
        elif a[i] != b:
            l[i] = -1
        else:
            l[i] = i
    return l


l = work(a, 'R')
r = work(a[::-1], 'L')[::-1]
print(sum((l[i] == -1 and r[i] == -1 or ((l[i] != -1 and r[i] != -1 and (n - r[i] - 1 + l[i] == 2 * i)) and a[i] == '.') for i in range(0, n))))
