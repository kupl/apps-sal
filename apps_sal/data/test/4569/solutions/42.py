lis = ["Sunny", "Cloudy", "Rainy"]
S = input()
x = lis.index(S)
if x == 2:
    ans_key = 0
else:
    ans_key = x + 1
print(lis[ans_key])
