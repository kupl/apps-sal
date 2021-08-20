def main():
    count = 0
    for i in range(1, n):
        if {a[i - 1], a[i]} == {2, 3}:
            return 0
        elif a[i - 1] == 3 and a[i] == 1:
            count += 4
        elif a[i - 1] == 2:
            count += 3
        elif i - 2 >= 0 and a[i - 2] == 3 and (a[i] == 2):
            count += 2
        elif a[i] == 2:
            count += 3
        else:
            count += 4
    return count


n = int(input())
a = list(map(int, input().split()))
p = main()
print('Finite\n{}'.format(p) if p else 'Infinite')
