X = int(input())
count = 0

kouka500 = X // 500 * 1000
count += kouka500

kouka5 = X % 500 // 5 * 5
count += kouka5

print(count)
