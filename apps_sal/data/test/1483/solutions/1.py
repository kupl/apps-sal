n = int(input())
l = list(map(int, input().strip().split()))
for i in range(1, n + 1):
    l1 = [0 for i in range(n + 1)]
    l1[i] = 1
    j = l[i - 1]
    while(True):
        if l1[j] == 0:
            l1[j] = 1
            j = l[j - 1]
        else:
            print(j, end=" ")
            break
print()
