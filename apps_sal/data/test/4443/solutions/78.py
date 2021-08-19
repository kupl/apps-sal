c = input()
cl = [chr(ord('a') + i) for i in range(26)]
print(cl[cl.index(c) + 1])
