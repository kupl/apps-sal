n = int(input())
arr = list(map(int, input().split()))
dic = {}
dic2 = {}
ansar = []
for i in range(n):
    dic[arr[i]] = 0
    dic2[arr[i]] = 0
    ansar.append(0)
count = 0
for i in range(n - 1, 0, -1):
    if dic[arr[i]] == 0:
        count += 1

        dic[arr[i]] = 1
    ansar[i - 1] = count
answer = 0
for i in range(n - 1):
    if dic2[arr[i]] == 0:
        answer += ansar[i]
        dic2[arr[i]] = 1
print(answer)
