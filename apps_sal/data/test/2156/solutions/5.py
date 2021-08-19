n = int(input())
arr = list(map(int, input().split()))
sumarray = [0] * (n + 1)
tot = 0
for i in range(n):
    tot += arr[i]
    sumarray[i + 1] = tot
# print(arr)
# print(sumarray)
q = int(input())
for i in range(q):
    l, r = list(map(int, input().split()))
    l -= 1
    temp = sumarray[r] - sumarray[l]
    print(temp // 10)
