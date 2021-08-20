ABC = input().split()
m = max(ABC)
ABC.remove(m)
print(eval(m + ABC[0] + '+' + ABC[1]))
