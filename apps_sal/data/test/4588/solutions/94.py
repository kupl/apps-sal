a,b = input().split()
a = a.replace("A","10").replace("B","11").replace("C","12").replace("D","13").replace("E","14").replace("F","15")
b = b.replace("A","10").replace("B","11").replace("C","12").replace("D","13").replace("E","14").replace("F","15")
if int(a) == int(b):
    print("=")
elif int(a) > int(b):
    print(">")
elif int(a) < int(b):
    print("<")
