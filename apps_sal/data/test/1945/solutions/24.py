a = int(input(''))
inputs = []
for value in range(a):
    a = input('').split(' ')
    inputs.append(a)
handles = []
guFat = []
for value in inputs:
    string = value[0] + ' ' + value[1]
    if value[0] not in handles:
        handles.append(value[1])
        guFat.append(string)
    if value[0] in handles:
        handles.remove(value[0])
        handles.append(value[1])
        for k in guFat:
            impor = k.split(' ')
            if value[0] == impor[1]:
                guFat.remove(k)
                guFat.append(impor[0] + ' ' + value[1])
print(len(handles))
for value in guFat:
    print(value)
