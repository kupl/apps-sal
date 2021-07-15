S = input()
T = input()
String1 = list(S)
String2 = list(T)
N = len(String1)



for i in range(1,N):
    if String1 == String2:
        print("Yes")
        break
    Ex = String1.pop()
    String1.insert(0,Ex)
    if String1 == String2:
        print("Yes")
        break
else:
    print("No")
