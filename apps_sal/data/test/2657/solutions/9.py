n = int(input())
aa = sorted(list(map(int, input().split())))
list1 = []
ma = aa[-1]
for i in range(n):
    d = abs(aa[i] - (ma + 1) // 2)
    list1.append([d, i])
md = min(list1, key=lambda x: x[0])
print(ma, aa[md[1]])
