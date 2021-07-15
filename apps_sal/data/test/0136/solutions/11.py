a = input()
b = input()
i = 0
j = 0
n = len(a)
m = len(b)
while i < n and a[i] == '0':
    i += 1
while j < m and b[j] == '0':
    j += 1
if n - i > m - j:
    print(">")
elif n - i < m - j:
    print("<")
else:
    while i < n:
        if a[i] > b[j]:
            print(">")
            break
        elif a[i] < b[j]:
            print("<")
            break
        else:
            i += 1
            j += 1
    else:    
        print("=")
