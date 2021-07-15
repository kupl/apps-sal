a = input()
a = int(a)
b = [0] * (a+1)
otv=0
b[0] = "hui pizda ebala blad perastan ypotreblat"
for i in range(a):
    b[i+1]=input()
for i in range(1,a+1):
    if b[i] != b[i-1]:
        otv += 1
print(otv)
