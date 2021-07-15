m = input("")
list = m.split(" ")
if eval(list[0])<10:
    print(eval(list[1])+100*(10-eval(list[0])))
if eval(list[0])>=10:
    print(eval(list[1]))
