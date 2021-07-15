n = int(input())
a = list(map(int, input().split()))
'''
b = []

front = False
for i in a:
    if front:
        b.insert(0, i)
        front = False
    else:
        b.append(i)
        front = True




if front:
    b.reverse()


b = list(map(str, b))
b = " ".join(b)
print(b)
'''


first = a[0:n:2]
last = a[1:n:2]
last = last[::-1]
answer = last + first
if n%2 != 0:
    answer = answer[::-1]

print(*answer, sep=" ")
