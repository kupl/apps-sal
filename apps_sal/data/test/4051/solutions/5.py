
# A
# print(int(input()) % 2)

# C
input()
a = [int(x) for x in input().split()]
while a:
    for i in range(len(a)-1):
        if abs(a[i] - a[i+1]) >= 2:
            print('NO')
            return
    i = a.index(max(a))
    a.pop(i)
print('YES')

