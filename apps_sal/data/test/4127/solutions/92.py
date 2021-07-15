a, b = map(str, input().split())
a, b = int(a), int(b.split(".")[0])*100 + int(b.split(".")[1])
print(a*b//100)
