X = int(input())
count1000 = X // 500
count5 = X % 500 // 5

print((count1000 * 1000 + count5 * 5))
