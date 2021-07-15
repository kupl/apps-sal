n = int(input())
a = input().split()
b = set(a)
maximum = -1
maximum_id = []
for i in b:
    x = a.count(i)
    if x > maximum:
        maximum_id = [int(i)]
        maximum = x
    elif x == maximum:
        maximum_id.append(int(i))
a = a[::-1]
maximum = -1
answer = -1
for i in maximum_id:
    x = a.index(str(i))
    if x > maximum:
        answer = i
        maximum = x
print(answer)
