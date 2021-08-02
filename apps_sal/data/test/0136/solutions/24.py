a = input()
b = input()
swap = 0
ans = ['<', '>']
if len(a) > len(b):
    a, b = b, a
    swap = 1
a = '0' * (len(b) - len(a)) + a
if a == b:
    print("=")
    quit()
if a < b:
    print(ans[swap])
    quit()
print(ans[1 - swap])
