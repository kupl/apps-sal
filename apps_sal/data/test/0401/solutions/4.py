l, lt = input().split()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b)
for i in a:
    if i in b:
        print(i)
        return
if min(a) < min(b):
    print(str(min(a)) + str(min(b)))
else:
    print(str(min(b)) + str(min(a)))
    



