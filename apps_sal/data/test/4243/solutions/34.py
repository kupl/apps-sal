X = int(input())
syou = int(X / 500)
syou_second = int((X - syou * 500) / 5)
ans = syou * 1000 + syou_second * 5
print(ans)
