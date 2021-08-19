n = int(input())
txt = input()
# print(type(n))
if len(txt) <= n:
    print(txt)
else:
    print(("%s..." % txt[:n]))
