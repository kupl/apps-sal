a = list(input())
b = list(input())
c = list(input())
abc = [a, b, c]
name = ['a', 'b', 'c']
now = 0
while True:
    if len(abc[now]) == 0:
        print((name[now].upper()))
        return
    now = name.index(abc[now].pop(0))
