def semifinals(l1, l2):
    output1 = [0] * len(l1)
    output2 = [0] * len(l2)
    n = len(l1)
    k = len(l1) // 2
    output1[0:k] = [1] * k
    output2[0:k] = [1] * k
    i = k
    while i < len(l1):
        if l1[i] < l2[n - i - 1]:
            output1[i] = 1
        if l2[i] < l1[n - i - 1]:
            output2[i] = 1
        i += 1
    output1 = ''.join([str(x) for x in output1])
    output2 = ''.join([str(x) for x in output2])
    return (output1, output2)


n = int(input())
l1 = []
l2 = []
for i in range(n):
    a = [int(x) for x in input().split()]
    l1.append(a[0])
    l2.append(a[1])
print(semifinals(l1, l2)[0])
print(semifinals(l1, l2)[1])
