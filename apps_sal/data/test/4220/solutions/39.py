n = int(input())
txt = input()
if len(txt) <= n:
    print(txt)
else:
    print('%s...' % txt[:n])
