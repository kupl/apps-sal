n = int(input())
kassu = list(map(int, input().split()))
products = []
for i in range(n):
   products +=  [list(map(int, input().split()))]
result = []
for i in range(n):
   test_result = 0
   for j in range(kassu[i]):
      test_result += products[i][j] * 5 + 15
   result.append(test_result)
print(min(result))
