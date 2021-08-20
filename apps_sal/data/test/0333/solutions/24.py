a = input()
b = input()
if len(a) != len(b):
    print(max(len(a), len(b)))
elif a != b:
    print(len(a))
else:
    print(-1)
