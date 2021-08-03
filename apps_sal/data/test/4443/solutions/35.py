c = input()
l = [chr(ord('a') + i) for i in range(26)]
print(l[l.index(c) + 1])
