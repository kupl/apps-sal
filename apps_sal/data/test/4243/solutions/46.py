#ABC160
X = int(input())
happiness = 0
happiness += (X // 500)*1000
X = X % 500
happiness += (X // 5)*5
print(happiness)
