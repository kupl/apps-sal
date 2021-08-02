n = int(input())
lst = []

for i in range(n):
    a = list(map(int, input().split()))
    lst.append(a)

lst.sort(key=lambda x: x[1])

time = 0

for i in lst:
    time += i[0]
    if time > i[1]:
        print('No')
        return


print('Yes')
