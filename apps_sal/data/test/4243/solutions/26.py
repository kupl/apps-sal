X = int(input())
gohyaku = X // 500
go = (X - gohyaku * 500) // 5
print(gohyaku * 1000 + go * 5)
