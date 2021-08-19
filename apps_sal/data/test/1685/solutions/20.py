def find(x):
    if root == x:
        u = root
    else:
        i = 0
        s = 2 ** i
        while x % s == 0:
            i += 1
            s = 2 ** i
        s = s // 2
        y = i + 1
        if (x - s) % 2 ** y != 0:
            u = x - s
        else:
            u = x + s
    return u


(n, q) = list(map(int, input().split()))
root = (n + 1) // 2
for j in range(q):
    n1 = int(input())
    str1 = input()
    for j in range(len(str1)):
        up = find(n1)
        if str1[j] == 'U':
            n1 = up
        elif n1 % 2 == 0:
            if str1[j] == 'L':
                if n1 != root:
                    n1 = n1 - abs((up - n1) // 2)
                else:
                    n1 = n1 - n1 // 2
            elif str1[j] == 'R':
                if n1 != root:
                    n1 = n1 + abs((up - n1) // 2)
                elif n1 % 2 == 0:
                    n1 = n1 + n1 // 2
    print(n1)
