n = int(input())
if n%2 == 1:
    result = 0
else:
    g =(n%4)+1
    h = 2**g+2
    result = h%5
print(result)

