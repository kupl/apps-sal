a, b = list(map(int, input().split()))

i = 1
while(i**2 <= a):
    i = i + 1
j = 1
while(j * (j + 1) <= b):
    j += 1

if i <= j:
    print("Vladik")
else:
    print("Valera")
