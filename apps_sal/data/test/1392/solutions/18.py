(n, k) = map(int, input().split())
ris = 0
for cont in range(0, n):
    num = input()
    l = True
    for tmp in range(0, k + 1):
        if (str(tmp) in num) is False:
            l = False
            break
    if l:
        ris += 1
print(ris)
