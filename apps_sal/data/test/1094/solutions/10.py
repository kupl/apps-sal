n = int(input())
a = [input() for i in range(n)]
was = set()
for name in a[::-1]:
    if name not in was:
        was.add(name)
        print(name)
