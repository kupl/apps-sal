n2 = input()
n = ""
n += n2[0]
n += n2[2]
n += n2[4]
n += n2[3]
n += n2[1]
n = int(n)
n = str(n**5)
print(n[len(n)-5:])

