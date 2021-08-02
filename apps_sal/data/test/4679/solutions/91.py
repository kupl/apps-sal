a = list(input())
b = list(input())
c = list(input())

D = {'a': a, 'b': b, 'c': c}
curr = 'a'
while True:
    tmp = D[curr]
    if tmp == []:
        break
    curr = tmp.pop(0)
print((curr.upper()))
