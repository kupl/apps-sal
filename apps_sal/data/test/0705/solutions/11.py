n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
s = set(x+y)

result = len([1 for xn in x for yn in y if xn^yn in s])
#for xn in x:
#    for yn in y:
#        result += xn^yn in s

print("Karen" if result%2==0 else "Koyomi")
