(x, y, z, K) = list(map(int, input().split()))
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)
c = sorted(list(map(int, input().split())), reverse=True)
lst = []
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            if (i + 1) * (j + 1) * (k + 1) > K:
                break
            lst.append(a[i] + b[j] + c[k])
new_lst = sorted(lst, reverse=True)
for i in range(K):
    print(new_lst[i])
