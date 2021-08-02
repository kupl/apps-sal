n = int(input())
a = [(int(el), i + 1) for i, el in enumerate(input().split())]
a = sorted(a, reverse=True)
shots = 0
for i, (el, _) in enumerate(a):
    shots += i * el + 1
print(shots)
print(*(i for _, i in a))
