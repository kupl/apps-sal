n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dic = {}
for i in range(n):
    dic[arr[i]] = dic[arr[i] + 1] + 1 if arr[i] + 1 in dic.keys() else 1
mx = 0
num = 0
for i in dic.keys():
    if dic[i] > mx:
        mx = dic[i]
        num = i
print(mx)
arr.reverse()
for i in range(n):
    if arr[i] == num:
        print(i + 1, end=' ')
        num += 1
