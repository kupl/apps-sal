import sys
K = int(input())
count = 0
nine = ""

arr = []
arr_sunuke = []
for k in range(14):
    for i in range(10):
        for j in range(10):
            for l in range(10):
                if i == 0 and nine != "":
                    pass
                else:
                    arr.append(int(str(i) + str(j) + str(l) + nine))
                    arr_sunuke.append(i + j + l + k * 9)
    nine = nine + str(9)

arr.remove(0)
arr_sunuke.remove(0)
arr_sunuke2 = [arr[i] / arr_sunuke[i] for i in range(len(arr))]

ans = []
tmp = 10**15
for i in range(len(arr) - 1, -1, -1):
    if arr_sunuke2[i] <= tmp:
        ans.append(arr[i])
        tmp = arr_sunuke2[i]

ans = ans[::-1]
for i in range(K):
    print(ans[i])
