import sys
s = input()

for i in range(97, 123):
    st = chr(i)
    if st not in s:
        print(st)
        return


print(None)
