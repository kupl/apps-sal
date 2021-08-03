a = input()
print(max(eval(a.replace(" ", k))for k in "+-*"))
