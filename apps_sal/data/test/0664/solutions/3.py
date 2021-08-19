n = int(input())
alist = [int(x) for x in input().split()]
fault = 0
for i in range(n):
    if alist[i - 1] <= alist[i]:
        pass
    else:
        fault += 1
        if fault > 1:
            print(-1)
            quit()
        f = i
if fault == 0:
    print(0)
    quit()
print((n - f) % n)
