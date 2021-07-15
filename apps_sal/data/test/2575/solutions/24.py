def ok(integer):
    if 360%(180-integer)==0:
        return "YES"
    else:
        return "NO"
stor=[]
sa=input()
for x in range(int(sa)):
    stor.append(ok(int(input())))
for element in stor:
    print(element)

