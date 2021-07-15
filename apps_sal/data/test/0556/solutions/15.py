l, r, k = map(int, input().split())
flag = 1
n = 1
while (n <= r) :
    if (n >= l) :
        print(n, end = " ")
        flag = 0
    n *= k
if (flag == 1) :
    print(-1)
