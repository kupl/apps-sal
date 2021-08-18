n = int(input())
s = list(map(int, input().split()))
strr = input()
dic = {}
for i in range(0, n):
    dic[s[i]] = i + 1
list0 = s[::]
list1 = []
list2 = []
m = ""
k = 0
j = 0
list0.sort()
for i in strr:
    if i == '0':
        m += str(dic[list0[j]]) + " "
        list1 += [list0[j]]
        k = k + 1
        j = j + 1
    else:
        m += str(dic[list1[k - 1]]) + " "
        del(list1[k - 1])
        k = k - 1
print(m)
