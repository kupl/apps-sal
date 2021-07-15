

n = int(input())

arr = [0] * (n + 2)
arr[0] = [-2000000001, -2000000001, 0]
arr[-1] = [2000000001, 2000000001, 0]
for i in range(1, n + 1):
   s = list(map(int, input().split()))
   arr[i] = [s[0], s[0], s[1]]
c = 0
for i in range(1, n + 1):
   if (arr[i - 1][0] < (arr[i][0] - arr[i][2])) and (arr[i - 1][1] < (arr[i][0] - arr[i][2])):
      arr[i][1] = arr[i][0] - arr[i][2]
      c += 1
   elif (arr[i + 1][0] > (arr[i][0] + arr[i][2])) and (arr[i + 1][1] > (arr[i][0] + arr[i][2])):
      arr[i][1] = arr[i][0] + arr[i][2]
      c += 1
      #print(i)
print(c)
